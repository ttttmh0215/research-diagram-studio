#!/usr/bin/env python3
"""Build portable Skill and Bradford-example archives from this checkout."""
from pathlib import Path
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / 'VERSION').read_text().strip()
SKILL = ROOT / 'skills' / 'cartoon-research-flowchart'
DIST = ROOT / 'dist'


def archive(destination, entries):
    with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED) as package:
        for source, name in sorted(entries, key=lambda item: item[1]):
            info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o644 << 16)
            package.writestr(info, source.read_bytes())
    with zipfile.ZipFile(destination) as package:
        if package.testzip() is not None:
            raise RuntimeError(f'Corrupt archive: {destination.name}')


def files_under(folder, prefix):
    entries = []
    for source in folder.rglob('*'):
        if not source.is_file() or source.is_symlink():
            continue
        if any(part in {'__pycache__', '.build', '.DS_Store'} for part in source.parts):
            continue
        if source.suffix == '.pyc':
            continue
        entries.append((source, prefix + source.relative_to(folder).as_posix()))
    return entries


def main():
    DIST.mkdir(exist_ok=True)
    skill_entries = files_under(SKILL, 'cartoon-research-flowchart/')
    skill_entries.append((ROOT / 'LICENSE', 'cartoon-research-flowchart/LICENSE'))
    skill_entries.append((ROOT / 'VERSION', 'cartoon-research-flowchart/VERSION'))
    archive(DIST / 'cartoon-research-flowchart.zip', skill_entries)
    archive(DIST / 'research-diagram-studio.zip', skill_entries)
    archive(DIST / 'bradford-example.zip', files_under(ROOT / 'examples/bradford', 'bradford-example/'))
    archives = sorted(DIST.glob('*.zip'))
    sums = [f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}' for p in archives]
    (DIST / 'SHA256SUMS.txt').write_text('\n'.join(sums) + '\n')
    for p in archives:
        print(f'v{VERSION}  {p.name}  {p.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()
