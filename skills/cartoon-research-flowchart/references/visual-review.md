# Two visual-review gates

Review actual images, not prompts or successful generation messages. The agent performs the initial review; the user then checks preferences and remaining errors. An image viewer, crop or comparison board supports review but cannot substitute for it.

## Gate A: after concept generation, before selection

Inspect the whole figure and then each panel/inset at useful scale.
- **Fidelity:** compare content, labels/formulas, conditions, counts and named connector endpoints with the paper/brief. Check material versus information paths and parallel versus sequential steps.
- **Intrinsic validity:** inspect legibility, geometric construction, face orientation, overlap/occlusion, repeated structures, complete contours and plausible scientific representations. Identify gibberish, impossible joins, unintended faces and untraceable arrows even if the prompt requested them accidentally.

Aesthetic preferences can remain open for user choice; scientific or construction defects that prevent interpretation are blockers. Inspect edited candidates again and store the actual version/hash.

## Gate B: after each asset, before usable delivery

First create a compact construction contract from the approved region: object identities, silhouette/arrangement, count if meaningful, intended perspective/parallelism, style, text omissions, boundaries and arrow anchors.

Inspect the reference region and generated asset side by side:
- **Fidelity:** has the object changed into a different construction? Check plane inclination, stacking order/spacing, thickness, palette, component proportions and tail/head/branch structure.
- **Intrinsic validity:** is this coherent on its own? Look for doubled or fused faces, accidental folds, inconsistent local perspective, cut edges, merged gaps, malformed symbols, residual lettering and unexplained parts.

A stack of intended parallel plates must preserve its parallel construction; an intentionally opened fan may have different angles. Do not turn a specific example into a requirement that every asset be parallel or 3D. If repetition is decorative, describe it as schematic; if it encodes a head/layer/sample count, check that count. If it cannot be counted reliably, mark it uncertain instead of claiming a verified count.

Inspect transparent images on a representative light background and a dark one, both close-up and at the intended placed size. RGB colors hidden under near-zero alpha can look alarming in some previews; judge correct compositing before calling them visible contamination. Check real alpha separately. Correct alpha and useful pixel dimensions say nothing about intrinsic correctness.

## Decisions and repair

Use `pass`, `needs_revision` or `uncertain` for each axis and record concrete observations, not just “looks good.” Any unresolved blocking issue prevents a ready/usable claim.

- Fidelity fails, intrinsic passes: repair drift toward the approved construction.
- Fidelity passes, intrinsic fails: do not copy the defect more faithfully. Revisit the intended construction and scientific brief, repair/regenerate the defective asset, and inspect it again.
- Both fail: rebuild the affected module from its source-grounded contract while preserving approved unaffected design.
- Source itself is wrong/ambiguous: record a source defect; do not label the asset/reference passed. Resolve against the paper. If correction changes approved scientific content or layout, show the corrected reference/version for approval unless existing authorization explicitly covers those edits and production. Pure asset repairs within the approved contract do not need repeated permission.
- If the approved reference itself fails, repairing an asset alone does not make that reference valid. Preserve the defective reference as a rejected revision; create and inspect a corrected reference too, then update its version, file hash and dependent asset reviews. Show the actual corrected reference and follow the existing scoped authorization; obtain new approval only where that authorization does not cover the correction. Until resolved, label any shown subset provisional/diagnostic rather than samples_ready. Never backfill a pass onto the defective file.
- Missing specialist information: ask only about the detail needed for correctness. Do not silently invent it or transform supplied evidence.

Default to at most **two targeted repair/regeneration attempts per failing item**. Stop earlier when additional input is needed; after the bound, mark it pending and explain the remaining problem. Keep rejected files for traceability outside the accepted set. Do not spend an open-ended loop on small aesthetics or call failed files completed.

If a host auto-displays raw image-tool results, identify them as unreviewed previews until checked; do not claim the tool hid them. Publish the reviewed comparison/contact sheet as the accepted set. Rejected items may be shown explicitly as diagnostics, not usable assets.

## State and user feedback

Bind every review to the exact inspected file/hash. Asset reviews also identify the approved reference hash. Regeneration or file changes invalidate the old record; a new successful tool call does not inherit a pass. The schema is in [manifest-and-delivery.md](manifest-and-delivery.md).

After Gate A, show reviewed concepts and ask which the user prefers and whether they see incorrect text, shapes, scientific relationships or anything to change. Wait for selection/production authorization.

After Gate B, show the reviewed assets and ask whether they see errors, mismatches or need changes. Honor the already authorized scope: a sample batch does not imply a full batch or PPT.

`validate_handoff.py` verifies presence, statuses and file/hash bindings of these records. It does not see images, evaluate observations, certify perspective, or guarantee scientific truth. Do not fabricate records merely to satisfy it.
