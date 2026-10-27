# State, inventory and delivery

The agent maintains records; the user chooses actual images and gives natural feedback. Use one project.json plus separate actual prompt files. New work uses schema_version 2. Existing schema-1 examples remain readable without pretending they passed the new review gates.

## Selection state

Record candidate IDs, styles, files, whether they were actually shown, visual-review decisions, selected_id, last_presented_id, feedback and production approval. A selected image is not automatically approved. Record the actual user statement and its scope. A planned revision is not a shown image; a newest file does not replace the chosen branch.

Stages: brief, review, revision, production, ready (full) or samples_ready (explicit sample subset). scope is full or sample. style is cartoon or geometric. Once an inspected file changes, its old visual review is stale.

## Inventory and assembly

For full scope perform both a region pass and a small-motif/inset/terminal pass. Distinguish unique assets from every repeated occurrence. An occurrence has id, asset_id and bbox [left, top, width, height] in canvas units. Keep the PPT/reference aspect ratio consistent.

Record assets as generated or provided, actual/planned/pending, with file, description, intended construction, optional minimum pixel size and actual hash. Supplied evidence needs its registration hash, preserved background reasons where applicable, and separately recorded requested transformations. Paths in the public handoff are package-relative.

Cartoon mode keeps native panels/labels/equations/connectors and empty illustration slots. Geometric mode generates compound shapes, frames and designed arrows; PPT frame.mode is text-placement with native labels/formulas and empty asset slots. A user-requested native override is allowed. Keep IDs out of publication-visible text; a guide may show them.

## Schema-2 production outline

This is a structural example, NOT an existing finished package. File paths, coordinates and review observations must come from actual work; null hashes and unreviewed decisions cannot pass validation.

```json
{
  "schema_version": 2,
  "scope": "full",
  "style": "geometric",
  "stage": "production",
  "selected_id": "G1-r2",
  "approved": {
    "id": "G1-r2",
    "file": "reference/approved.png",
    "sha256": null,
    "user_statement": "Use this version; make the assets and PPT."
  },
  "canvas": {"width": 1800, "height": 1100, "unit": "px"},
  "assets": [
    {"id": "A01", "kind": "generated", "role": "geometry",
     "file": "assets/A01.png", "status": "planned",
     "construction": "One coherent source-grounded geometric module",
     "min_size_px": [600, 600]}
  ],
  "occurrences": [
    {"id": "O01", "asset_id": "A01", "bbox": [100, 150, 400, 300]}
  ],
  "native_elements": [{"id": "N01", "kind": "text", "label": "Input"}],
  "coverage_review": {"region_pass": false, "small_motif_pass": false},
  "frame": {"file": "frame.pptx", "status": "planned", "mode": "text-placement",
            "native_labels": ["Input"]},
  "visual_reviews": {
    "reference": {
      "file": "reference/approved.png", "sha256": null,
      "fidelity": {"status": "unreviewed", "observations": []},
      "intrinsic": {"status": "unreviewed", "observations": []},
      "issues": []
    },
    "assets": [
      {"asset_id": "A01", "file": "assets/A01.png", "sha256": null,
       "reference_sha256": null,
       "fidelity": {"status": "unreviewed", "observations": []},
       "intrinsic": {"status": "unreviewed", "observations": []},
       "issues": []}
    ]
  },
  "delivery": {
    "contact_sheet": "asset-contact-sheet.png",
    "placement_guide": "placement-guide.md",
    "assembly_guide": "ASSEMBLY.md",
    "prompts_index": "prompts/index.json",
    "frame_preview": "frame-preview.png"
  }
}
```

After actually inspecting a file, set each review axis to pass, needs_revision or uncertain with concrete observations. For a concept, fidelity is to paper/brief; for an asset, it is to the approved source region/construction. Intrinsic validity is independent in both cases. Each issue is an object with severity (blocking/minor), status (open/resolved), and a nonempty description. Ready requires both axes passed and no open blockers; malformed issue entries are rejected.

Compute sha256 from the actual inspected files. Each asset review also records the actual approved reference_sha256. A renamed, regenerated, changed or newly based asset needs a new review; the validator rejects stale/missing file/hash bindings.

## Sample-only branch

When explicitly requested, use scope: sample and finish at samples_ready. Register only the requested actual asset subset and its reviews, the selected reference with review/hash, a canvas, contact_sheet and prompts_index. Occurrences are optional; if supplied their boxes must be valid. A sample needs no PPT, native_elements, full-coverage flags, placement guide or assembly guide. Do not call it the complete figure handoff.

## Asset quality

Pixels ≈ printed width_mm / 25.4 × dpi. Prefer about 600 dpi for small line-art assets where feasible, with at least 300 dpi or the user's threshold. Real alpha needs transparent and visible pixels; a painted checkerboard is not alpha. Inspect correctly composited light/dark views for halos, clipping and stray pixels. Do not remove meaningful evidence backgrounds to force transparency.

## Delivery and validation

Full package: approved reference, reviewed assets, contact sheet, empty frame, frame preview, project.json, placement/assembly guides and actual prompts. If frame rendering is unavailable, record frame_preview: null and the actual frame_preview_unavailable_reason. Report native counts and actual rendering scope without calling raster illustration internals editable.

Run:
```bash
python scripts/validate_handoff.py figure-package/project.json --report verification.json
```

The script checks files, alpha, optional minimum pixels, occurrences, approval, PPT aspect/native inventory and absence of artwork images/media in the empty frame. Schema 2 additionally checks the two visual-review decisions, observations, unresolved blockers and file/reference hash bindings. These are provenance checks, NOT automated visual reasoning. A syntactically valid report cannot prove geometry or science correct; never manufacture observations to make it pass.
