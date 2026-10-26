#!/usr/bin/env python3
"""Read-only checks for a cartoon figure's manual-assembly handoff package."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import unicodedata
import xml.etree.ElementTree as ET
import zipfile


def validate(project_path: Path) -> dict:
    project = json.loads(project_path.read_text(encoding='utf-8'))
    root = project_path.resolve().parent
    errors, warnings, assets_report = [], [], []

    def existing(relative, role):
        if not isinstance(relative, str) or not relative:
            errors.append(f'{role}: no file recorded')
            return None
        path = root / relative
        if Path(relative).is_absolute() or not path.resolve().is_relative_to(root):
            errors.append(f'{role}: use a package-relative path')
            return None
        if not path.is_file():
            errors.append(f'{role}: missing file {relative}')
            return None
        return path

    if project.get('stage') != 'ready':
        errors.append('The manifest is not at the ready stage; do not claim a completed handoff')
    approved = project.get('approved') or {}
    if not approved.get('id') or not str(approved.get('user_statement', '')).strip():
        errors.append('A specific approved version and actual user approval statement are required')
    if approved.get('id') != project.get('selected_id'):
        errors.append('Selected and approved version IDs differ')
    reference = existing(approved.get('file'), 'approved reference')
    if reference and approved.get('sha256'):
        if hashlib.sha256(reference.read_bytes()).hexdigest() != approved['sha256']:
            errors.append('Approved reference hash mismatch')

    canvas = project.get('canvas', {})
    cw, ch = canvas.get('width'), canvas.get('height')
    number = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)
    canvas_ok = number(cw) and number(ch) and cw > 0 and ch > 0 and bool(canvas.get('unit'))
    if not canvas_ok:
        errors.append('Canvas needs positive width/height and a declared coordinate unit')

    assets = project.get('assets', [])
    asset_ids = [a.get('id') for a in assets]
    if len(asset_ids) != len(set(asset_ids)) or any(not x for x in asset_ids):
        errors.append('Asset IDs must be nonempty and unique')
    for asset in assets:
        aid = asset.get('id')
        if asset.get('status') != 'actual':
            errors.append(f'{aid}: asset is still planned or pending')
        kind = asset.get('kind')
        if kind not in ['generated', 'provided']:
            errors.append(f'{aid}: kind must be generated or provided')
        path = existing(asset.get('file'), str(aid))
        if not path:
            continue
        if asset.get('sha256'):
            if hashlib.sha256(path.read_bytes()).hexdigest() != asset['sha256']:
                errors.append(f'{aid}: asset/source-copy hash mismatch')
        elif kind == 'provided':
            warnings.append(f'{aid}: provided-source identity has no recorded hash')
        if kind == 'generated' and path.suffix.lower() != '.png':
            errors.append(f'{aid}: generated artwork must be a transparent PNG')
        if path.suffix.lower() in ['.svg', '.pdf', '.eps'] and kind == 'provided':
            assets_report.append({'id': aid, 'file': asset['file'], 'provided_vector': True})
            continue
        try:
            from PIL import Image
            with Image.open(path) as image:
                alpha = image.convert('RGBA').getchannel('A')
                low, high = alpha.getextrema()
                transparent = low < 255 and high > 0
                if (kind == 'generated' or asset.get('require_alpha')) and not transparent:
                    errors.append(f'{aid}: no usable actual alpha transparency')
                if kind == 'provided' and not transparent and not asset.get('preserve_background_reason'):
                    warnings.append(f'{aid}: opaque supplied image; record why its background is retained')
                minimum = asset.get('min_size_px')
                if minimum is not None:
                    if not (isinstance(minimum, list) and len(minimum) == 2
                            and all(number(n) and n > 0 for n in minimum)):
                        errors.append(f'{aid}: invalid min_size_px')
                    elif image.width < minimum[0] or image.height < minimum[1]:
                        errors.append(f'{aid}: output is below the recorded minimum pixel size')
                assets_report.append({'id': aid, 'file': asset['file'],
                                      'size': list(image.size), 'alpha_extrema': [low, high],
                                      'actual_transparency': transparent})
        except (OSError, ImportError, ValueError) as exc:
            errors.append(f'{aid}: cannot inspect raster asset: {exc}')

    occurrences = project.get('occurrences', [])
    occurrence_ids, used_assets = [], set()
    for occurrence in occurrences:
        oid, aid = occurrence.get('id'), occurrence.get('asset_id')
        occurrence_ids.append(oid)
        if aid not in asset_ids:
            errors.append(f'{oid}: artwork occurrence references missing asset {aid}')
        else:
            used_assets.add(aid)
        box = occurrence.get('bbox')
        valid = isinstance(box, list) and len(box) == 4 and all(number(n) for n in box)
        if not valid:
            errors.append(f'{oid}: invalid [left,top,width,height] box')
        elif min(box[:2]) < 0 or min(box[2:]) <= 0 or (canvas_ok and
                (box[0] + box[2] > cw + 1e-6 or box[1] + box[3] > ch + 1e-6)):
            errors.append(f'{oid}: placement is empty or outside the canvas')
    if len(occurrence_ids) != len(set(occurrence_ids)) or any(not x for x in occurrence_ids):
        errors.append('Occurrence IDs must be nonempty and unique')
    for aid in set(asset_ids) - used_assets:
        warnings.append(f'{aid}: delivered asset has no recorded placement')
    if not project.get('native_elements'):
        errors.append('Record the native structure separately from artwork occurrences')
    review = project.get('coverage_review', {})
    if not review.get('region_pass') or not review.get('small_motif_pass'):
        errors.append('Both region-wide and small-motif inventory passes must be completed')

    frame = project.get('frame', {})
    if frame.get('status') != 'actual':
        errors.append('PPT frame is still planned or pending')
    pptx = existing(frame.get('file'), 'empty PPT frame')
    ppt_report = None
    if pptx:
        try:
            ns = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
                  'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
            with zipfile.ZipFile(pptx) as archive:
                corrupt = archive.testzip()
                if corrupt:
                    errors.append(f'PPTX archive is corrupt: {corrupt}')
                slide_names = sorted(n for n in archive.namelist()
                                     if re.fullmatch(r'ppt/slides/slide\d+\.xml', n))
                totals = {'slides': len(slide_names), 'native_shapes': 0,
                          'native_connectors': 0, 'pictures': 0, 'image_fills': 0}
                texts = []
                for name in slide_names:
                    tree = ET.fromstring(archive.read(name))
                    totals['native_shapes'] += len(tree.findall('.//p:sp', ns))
                    totals['native_connectors'] += len(tree.findall('.//p:cxnSp', ns))
                    totals['pictures'] += len(tree.findall('.//p:pic', ns))
                    totals['image_fills'] += len(tree.findall('.//a:blip', ns))
                    texts.extend(t.text or '' for t in tree.findall('.//a:t', ns))
                media = [n for n in archive.namelist() if n.startswith('ppt/media/') and not n.endswith('/')]
                totals['media_files'] = len(media)
                if not slide_names or not totals['native_shapes'] + totals['native_connectors']:
                    errors.append('PPT has no native editable structure')
                if totals['pictures'] or totals['image_fills'] or media:
                    errors.append('The manual-assembly frame contains pictures or image media; artwork must remain empty')
                normalized = lambda s: re.sub(r'\s+', '', unicodedata.normalize('NFKC', s))
                text_content = normalized(' '.join(texts))
                expected_labels = set(frame.get('native_labels', []))
                expected_labels.update(n['label'] for n in project.get('native_elements', [])
                                       if n.get('kind') == 'text' and n.get('label'))
                for label in expected_labels:
                    if normalized(label) not in text_content:
                        errors.append(f'Expected native text is missing: {label}')
                pres = ET.fromstring(archive.read('ppt/presentation.xml'))
                size = pres.find('p:sldSz', ns)
                if size is not None and canvas_ok:
                    ratio = int(size.attrib['cx']) / int(size.attrib['cy'])
                    if not math.isclose(ratio, cw / ch, rel_tol=0.01):
                        errors.append('PPT slide aspect ratio differs from the declared canvas')
                ppt_report = totals
        except (OSError, zipfile.BadZipFile, ET.ParseError, KeyError, ZeroDivisionError) as exc:
            errors.append(f'Cannot inspect PPTX: {exc}')

    delivery = project.get('delivery', {})
    for key in ['contact_sheet', 'placement_guide', 'assembly_guide', 'prompts_index']:
        existing(delivery.get(key), key)
    if delivery.get('frame_preview'):
        existing(delivery['frame_preview'], 'frame preview')
    elif not delivery.get('frame_preview_unavailable_reason'):
        errors.append('Provide a rendered frame preview or its actual unavailability reason')
    else:
        warnings.append('Frame rendering unavailable: ' + delivery['frame_preview_unavailable_reason'])

    return {'passed': not errors, 'errors': errors, 'warnings': warnings,
            'unique_assets': len(assets), 'artwork_occurrences': len(occurrences),
            'assets': assets_report, 'ppt': ppt_report,
            'scope': 'Manifest/file/alpha/pixel/PPT checks only; visual omissions, semantic correctness and rendering require separate review.'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path, help='The delivery folder project.json')
    parser.add_argument('--report', type=Path, help='Optional JSON report file')
    args = parser.parse_args()
    try:
        result = validate(args.project)
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        result = {'passed': False, 'errors': [f'Cannot read manifest: {exc}']}
    text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(text, encoding='utf-8')
    print(text, end='')
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
