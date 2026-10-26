# Review state, full-figure inventory and delivery

The assistant maintains these records; the user should review images and express preferences naturally, not fill JSON forms. One `project.json` can hold the small state and final manifest, with actual prompts in separate files.

## Review state

```json
{
  "schema_version": 1,
  "stage": "review",
  "brief_file": "paper-brief.md",
  "candidates": [
    {"id": "A-r1", "file": "previews/A-r1.png", "status": "actual", "presented": true},
    {"id": "B-r1", "file": "previews/B-r1.png", "status": "actual", "presented": true},
    {"id": "C-r1", "file": "previews/C-r1.png", "status": "actual", "presented": true}
  ],
  "selected_id": "B-r1",
  "last_presented_id": "C-r1",
  "approved": null,
  "feedback": [
    {"base_id": "B-r1", "keep": ["layout"], "change": ["use A's palette"]}
  ],
  "frame": {"file": "frame.pptx", "status": "planned"}
}
```

Use `brief`, `review`, `revision`, `production` and `ready` as stage labels. `status: actual` means a file exists, not that the user has approved it. Store the accepted version and concise user approval wording in `approved`; do not infer it from a selected ID alone.

`last_presented_id` records the last actual image shown; an explicit user selection may refer to an earlier shown image. Resolve pronouns against that context and the current selected branch. A merely planned `B-r2` cannot be described as already shown or approved. An explicit instruction to apply specified edits and proceed without further review is scoped authorization; keep that distinct from having viewed a new image.

When the user combines concepts, generate a new revision, record its parent(s), show it and follow their instructions about acceptance. Keep old versions available. Resume the selected branch rather than the newest file in a directory.

## Full-figure inventory

Start with a region checklist covering every panel. Then sweep across titles, corners, insets, terminals, legends, repeated motifs and small explanatory scenes. Record what becomes native structure and what becomes an asset.

Two different counts matter:

- **Unique assets**: actual distinct files to deliver.
- **Occurrences**: every placement in the approved figure, including repeated uses of one asset.

Each artwork occurrence needs an asset ID and bounding box. Each native component needs a native-element record. A compound panel can contain both. Explicitly describe any agreed removal; a missing element is not an omission decision.

Suggested compact production fields:

```json
{
  "schema_version": 1,
  "stage": "production",
  "selected_id": "B-r2",
  "approved": {
    "id": "B-r2",
    "file": "reference/approved.png",
    "sha256": "optional-actual-file-digest",
    "user_statement": "Use this one; make the assets and empty PPT frame."
  },
  "canvas": {"width": 1800, "height": 1100, "unit": "px"},
  "assets": [
    {
      "id": "A01",
      "kind": "generated",
      "file": "assets/A01_subject.png",
      "status": "planned",
      "description": "A paper-specific cartoon subject",
      "min_size_px": [600, 600]
    },
    {
      "id": "A02",
      "kind": "provided",
      "file": "assets/A02_source_panel.png",
      "status": "planned",
      "preserve_background_reason": "Background belongs to the supplied scientific image."
    }
  ],
  "occurrences": [
    {"id": "O01", "region": "R01", "asset_id": "A01", "bbox": [80, 120, 180, 180]},
    {"id": "O02", "region": "R02", "asset_id": "A01", "bbox": [720, 120, 180, 180]},
    {"id": "O03", "region": "R03", "asset_id": "A02", "bbox": [1100, 150, 500, 350]}
  ],
  "native_elements": [
    {"id": "N01", "kind": "text", "label": "Input"},
    {"id": "N02", "kind": "connector", "from": "input", "to": "processor"}
  ],
  "coverage_review": {
    "region_pass": false,
    "small_motif_pass": false,
    "notes": "Complete both visual sweeps before final delivery."
  },
  "frame": {"file": "frame.pptx", "status": "planned", "native_labels": ["Input"]},
  "delivery": {
    "contact_sheet": "asset-contact-sheet.png",
    "placement_guide": "placement-guide.md",
    "assembly_guide": "ASSEMBLY.md",
    "prompts_index": "prompts/index.json",
    "frame_preview": "frame-preview.png"
  }
}
```

This is an example, not an actual produced package. Replace dimensions, labels, IDs, paths, minimum sizes and the optional digest with real project values. Omit the `sha256` field until it is actually computed. Set `ready` only when actual production and verification have finished. If frame rendering is unavailable, use `frame_preview: null` and record `frame_preview_unavailable_reason` in `delivery`.

All production asset files should be inside the delivery folder and referenced by relative paths. Generated artwork is PNG with actual transparency. Provided images/vectors remain identified as provided sources. A provided SVG or PDF can be preserved as a source asset even when the alpha-check script cannot raster-inspect it.

For unchanged supplied evidence, compute its SHA256 at registration and store it as the asset's `sha256`; the validator checks the delivered copy against that digest. If a user-requested transformation is needed, retain the original and record the operation, source digest and delivered-file digest separately. File identity does not replace visual interpretation, but it prevents accidentally delivering a generated look-alike as the supplied evidence.

## Spatial correspondence

`bbox` is `[left, top, width, height]` in the declared canvas unit. Record every reuse. Convert coordinates consistently when authoring PowerPoint; check that its slide aspect ratio matches the reference canvas.

Keep each placement empty in the main frame. An optional guide can show numbered placements over a separate preview, or list coordinates and sizes. Avoid visible asset IDs in the publication frame. Say which supplied image goes in which slot.

## Asset quality

Choose output pixels from the intended print width and desired effective resolution: pixels ≈ width_mm / 25.4 × dpi. Prefer around 600 dpi for small line-art assets when feasible, with at least 300 dpi or the user's specified threshold. `min_size_px` lets the validator check the requested minimum; a user still needs to inspect line sharpness, padding and scientific fidelity.

True alpha requires transparent and visible pixels; a checkerboard drawn on an opaque canvas fails this test. A correct alpha channel does not alone establish that edges are clean. Do not remove the meaningful background from evidence to force a transparency claim.

## Final handoff

```text
figure-package/
├── reference/approved.png
├── assets/...
├── frame.pptx
├── frame-preview.png
├── asset-contact-sheet.png
├── placement-guide.md
├── ASSEMBLY.md
├── project.json
└── prompts/...
```

Explain the manual assembly steps briefly: open the native frame; insert each asset using the guide; preserve its aspect ratio; adjust size and alignment; reuse the same asset at repeated placements; inspect arrows and text; save an assembled copy; export the final figure at the paper size. The main frame remains a separate clean source.

Run `python scripts/validate_handoff.py /path/to/figure-package/project.json --report /path/to/verification.json`. The script checks files, generated alpha, optional minimum pixels, occurrence references/boxes, approval record, frame aspect and native object inventory. It also rejects pictures, image fills and image media in the empty frame. It does not detect an unlisted visual element or judge scientific meaning; the two visual inventory passes and native rendering remain necessary.
