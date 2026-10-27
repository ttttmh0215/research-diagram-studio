# Stage-specific prompt templates

Expand templates from the current paper and actual feedback; save the submitted prompts. Stable IDs and the selected style belong in each prompt. Do not reuse historical subjects, palettes or asset counts.

## P1 — Scientific brief

Read {paper_or_method}. Extract the research problem, exact terms/formulas, inputs/outputs, modules, order, parallel paths, conditions, shared components and feedback. Create concise visible labels and a typed node/edge contract with named endpoints. Plan panel hierarchy, typography, palette roles, source images and intended publication size. Separate scientific facts from design choices; ask only about missing facts affecting correctness.

## P2 — Candidate set

Using one scientific brief, create {requested_count_and_styles}; default two cartoon and two geometric concepts. Vary composition, palette, construction and visual weight while preserving the same scientific content. A new layout must not invent a loop, measured result or causal claim. Call image generation separately for each candidate.

## P3 — One complete reference image

```text
Create ONE complete scientific workflow/method reference figure.
ID {candidate_id}; style {cartoon_or_geometric}; canvas {aspect_ratio};
publication size {size}; language {language}.

SCIENTIFIC CONTRACT
{typed_nodes_edges_conditions_and_shared_components}
EXACT LABELS
{labels_and_formulas}
COMPOSITION
{panel_structure_reading_order_and_source_image_roles}
STYLE
{cartoon_subjects_OR_geometric_constructions}
{palette_tonal_hierarchy_type_roles_and_visual_weight}
{arrow_roles_named_sources_destinations_and_routing}

Preserve supplied evidence in its actual source files; generated renderings of
those sources are not authoritative evidence. Transfer only requested visual
features from style references, not unrelated text, logos or results.
Return a full composed concept, not separate assets.
```

For cartoon work retain the existing recognizable scientific subjects and disciplined comic language. For geometric work use [geometric-composition.md](geometric-composition.md): flat faces, lightly shadowed planes, stacks, fans, trapezoid assemblies, matrices and varied designed arrows according to content. Do not force every module into an equally thick cuboid.

## P3a — Concept visual review

Assistant review instruction after generation, before presenting a ready candidate:

```text
Inspect actual file {candidate_file} against {paper_and_brief}.
Report two separate decisions with concrete observations:
fidelity — content, labels, formulas, meaningful counts and connector endpoints;
intrinsic — coherent construction, face/occlusion relations, legibility and
plausible scientific representation independent of resemblance to a reference.
Inspect the whole image and each inset. Mark pass / needs_revision / uncertain.
Repair blockers within the bounded policy and inspect the replacement file.
Record the actual version/hash; do not inherit a pass from an earlier image.
```

## P4 — User selection and error feedback

Show reviewed images with IDs, then ask naturally, for example:

> 你更喜欢哪一张？图里的文字、形状或科学关系有没有错误，或者哪里想调整？可以直接说“保留 B 的结构，用 A 的颜色”；满意后告诉我继续做素材即可。

Wait for the answer. Do not treat an asynchronous question return, silence or timeout as approval. Respect existing approval and instructions authorizing specified edits plus production.

## P5 — Bounded revision

```text
Edit {selected_base_id_and_file}.
Actual feedback: {user_feedback}.
Preserve {approved_layout_palette_labels_subjects_and_relations}.
Change only {affected_regions_constructions_or_named_connector_endpoints}.
Scientific invariants: {affected_source_grounded_relations}.
Return a revised full reference; preserve other regions.
```

For fresh generation carry forward the scientific contract and chosen visual features. Re-review and show the revision; follow the user's actual authorization scope for production.

## P6 — Inventory

Inspect the approved figure region by region and sweep small motifs, insets and terminals. Register unique assets and every occurrence separately. Record source regions, semantic roles, bounding boxes, meaningful counts and constructions. In cartoon mode titles/panels/arrows are native; in geometric mode compound frames/shapes and designed arrows are assets while text/formulas remain native. If only samples are requested, inventory the authorized subset and do not trigger full production.

## P7 — One transparent asset

```text
Create ONE isolated transparent PNG for PowerPoint.
ID {asset_id}; role {illustration_geometry_frame_or_arrow}.
Source region {approved_reference_region}; intended construction {contract}.
Match {palette_outline_perspective_shading_and_identity}.
Preserve {component_count_arrangement_faces_silhouette_and_arrow_endpoints}.
Complete subject and edges, useful transparent padding, real alpha.
No text, labels, formulas, watermark or unrelated outer panel.
Target pixels/print size {actual_requirement}.
Return this coherent asset only, not the full figure or a sprite sheet.
```

Set the actual transparency flag. A registered arrow/frame includes its intended geometry; other illustration assets omit workflow connectors. Do not regenerate experimental evidence. Compare source construction with the scientific brief before copying a source defect.

## P7a — Asset visual review

```text
Inspect {actual_asset_file} beside {approved_reference_region} and {construction_contract}.
First decide fidelity: same intended components, arrangement, meaningful count,
relative size, silhouette, perspective, palette and connector endpoints?
Then decide intrinsic validity: coherent faces/stacking/occlusion, no unintended
folds, broken edges, gibberish, extra parts, cropped tips or scientific errors?
Inspect on light and dark backgrounds and at placed size; distinguish actual
composited defects from RGB artifacts under near-zero alpha.
A faithful copy of a bad source still fails. State concrete observations.
Repair or regenerate blockers, then inspect the new file and update its hash.
```

Follow [visual-review.md](visual-review.md) for bounded retries, source defects and uncertainty. Show the reviewed samples and ask whether the user sees errors or needs changes.

## P8 — Empty PPT frame

```text
Build an editable PowerPoint assembly frame for {approved_id}.
Selected mode {native_or_text_placement}; canvas {dimensions_units}.
Cartoon/native: native panels, labels, equations, blocks and workflow connectors.
Geometric/text-placement: native labels/formulas and overall placement layout;
reserve the generated shapes, frames and arrows as empty artwork slots.
Use {available_fonts}, {exact_labels}, {placements}, {relative_scales_and_anchors}.
Do not embed artwork, the full reference, hidden pictures or a slide bitmap.
Keep IDs in object names or the separate guide. Preserve user-edited files.
Export the empty frame, actual rendered preview and useful placement guide.
```

Only run this when PPT/full production is authorized. State the actual rendering scope.

## P9 — Handoff

Reconcile authorized files and occurrences. Run the technical validator and inspect actual visual-review records bound to current files. Deliver reference, reviewed assets/contact sheet, actual prompts and the records. For full scope add the empty PPT, preview, coordinates and assembly instructions. For samples explicitly identify the subset without a PPT/full-coverage claim. Verify archive contents, and ask the user whether they find errors or want adjustments.
