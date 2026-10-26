# Prompt templates for the three-stage workflow

Construct these prompts from the current paper and user feedback. Braced fields are parameters. Do not replay a historic case prompt or assume a fixed discipline, number of panels, model roles, font or asset count.

## P1 — Extract the scientific backbone and drawing brief

Assistant instruction, not an image-tool prompt:

```text
Read {paper_or_method_source} and the user's figure ideas.
Extract the research question, key contribution, inputs/outputs, essential
modules, order, alternatives, parallel paths, conditions, feedback and shared
components. Preserve exact terminology, equations and source-based results.

Create concise visible labels and a typed node/edge list. Move explanatory
prose to a caption note when it does not need to be drawn. Do not impose a
fixed word-reduction ratio or remove conditions that define the method.

Prepare a drawing brief for {language_and_publication_size}: panel hierarchy,
label list, font roles, palette roles, meaningful cartoon subjects, supplied
images/subfigures, and exact structures that require native/source-based drawing.
Separate scientific facts from layout choices. Ask only about unresolved details
that prevent a correct figure; do not ask the user to fill the whole brief.
```

## P2 — Design a varied candidate set

Assistant instruction:

```text
Using the same scientific brief, design {candidate_count_default_three}
cartoon/comic research figure concepts. Give each a stable ID.
Vary layout, palette, and illustration treatment together. Every concept must
express the same modules and scientific relationships.

For each concept, specify its composition, color roles, font roles, cartoon
subjects, supplied-image placements, and one concrete reason it suits the method.
Do not invent a cycle, comparison, causal claim or measured result to justify
a different layout. Use the user's visual references only for the requested
style features. Then submit each concept separately to image generation.
```

## P3 — Generate one cartoon reference image

Image-tool prompt; expand separately for each concept:

```text
Create ONE polished cartoon/comic scientific workflow reference image.
Concept: {candidate_id}. Canvas: {aspect_ratio}. Background: {background}.
Intended publication size: {target_size}. Language: {language}.

SCIENTIFIC CONTENT — preserve these relationships
{compact_node_edge_condition_and_shared_component_contract}

EXACT VISIBLE LABELS
{short_label_list_and_formulas}

COMPOSITION AND STYLE
{candidate_specific_panel_structure_and_reading_order}
{candidate_specific_palette_font_roles_and_cartoon_illustration_treatment}
Use recognizable subjects: {illustration_subjects}.
Keep panel hierarchy, text and paths readable at the target width.
Keep scientific arrowheads at destinations; avoid ambiguous crossings and
extra loops. Use moderately expressive cartoon art with disciplined layout.

REFERENCE ROLES
{content_reference_role}
{style_reference_roles}
{provided_images_and_fixed_source_panel_placements}
Do not transfer unrelated text, logos, numbers or method content from a style
reference. Supplied scientific images remain authoritative in their original
files even if this concept render simplifies their appearance.

This is a complete visual reference for user review, not a claim that its
generated text or evidence has already been verified for final publication.
```

## P4 — Ask for user preference after showing the images

Use natural language in the user's language. Example:

> 你更喜欢哪一张？可以直接采用，也可以说“保留B的结构，用A的颜色”，或指出想改的文字、图案和局部结构；需要的话，我会沿选中的风格再生成一版。满意后告诉我继续拆素材和做PPT框架即可。

Display stable IDs and actual images before this question. Wait for the answer. If the environment has an asynchronous question tool, use it and keep the task at the review stage; do not treat its return or a timeout as user approval.

## P5 — Refine the chosen version from actual feedback

```text
Edit {selected_base_id_and_revision}, using the supplied image as the base.
The user's current feedback is: {actual_feedback}.

PRESERVE
{user_requested_keep_layout_palette_labels_subjects_and_connections}

CHANGE
{bounded_changes_with_region_and_named_endpoints}
{elements_to_borrow_from_other_selected_concepts_if_any}

Maintain the scientific contract: {affected_relations}.
Approximate coordinates locate the edit; scientific node identities define
the correct endpoints. Return the revised complete reference image.
Do not modify unrelated regions or invent a new method.
```

For a requested same-style regeneration, replace “Edit” with a new-image instruction that explicitly carries forward the chosen style, content contract and requested changes. Present the new result for review before production. An earlier image's approval does not approve a new unseen image. Only an explicit user instruction to apply specified edits and proceed without another review changes that sequence; record its scope accurately.

## P6 — Inventory every illustration and subfigure

Assistant instruction after approval:

```text
Inspect the exact approved reference {approved_id_and_file} region by region.
Inventory EVERY illustration, inset subfigure, micro-scene, photo region,
data/evidence panel, small corner motif, legend symbol, terminal-branch image
and repeated occurrence. Do not restrict the inventory to supplied crops.

For each occurrence, record ID, parent region, semantic purpose, bounding box
in a declared coordinate system, unique asset or native element ID, and treatment.
Treatments: generate transparent illustration; reuse supplied source; draw exact
native/vector structure; or explicitly agreed omission.

For mixed subfigures, split native titles/labels/panels/arrows from inner artwork.
Reuse identical artwork across placements, and register every placement.
Make a second sweep for small motifs and end branches. Reconcile all regions
against the occurrence table before generating the batch.
```

## P7 — Generate one high-resolution transparent asset

```text
Create ONE standalone transparent PNG asset for manual placement in PowerPoint.
Asset ID: {asset_id}. Intended subject: {subject_and_role}.
Use {approved_reference_or_matching_asset} only for its visual style and identity.

COMPOSITION
{complete_objects_order_pose_perspective_relative_scale_and_aspect_ratio}
Match {outline_palette_shading_and_cartoon_style}.
Keep the whole subject complete, with useful transparent margins; do not crop
{critical_edges_or_parts}. Target size: {required_pixel_dimensions_or_print_size}.

ISOLATION
Use real alpha transparency, including blank space between isolated objects.
No outer panel, white rectangle, checkerboard pattern, card background,
title, label, formula, watermark or workflow connector.
{existing_symbols_and_editable_text_to_omit}
Return only this semantic asset, not the full reference figure or a sprite sheet.
```

Set the actual tool transparency flag. For asset edits, preserve existing transparency and modify only the user-requested details. Do not use this template to regenerate experimental evidence.

## P8 — Build the editable frame with all artwork positions empty

Presentation-authoring instruction:

```text
Reconstruct the approved reference {approved_id} as a native editable PowerPoint
FRAME for the user to assemble manually. Use {canvas_dimensions_and_units}.

Create every non-artwork element using native shapes/text/equations/vectors:
background, panels, fills, titles, labels, formulas, subfigure labels, legend
labels, lines, arrows, decision symbols and forks. Follow {scientific_contract}
and {exact_label_list}. Use {available_font_roles_and_sizes}.

Reserve every artwork occurrence from {manifest}: {placements_and_dimensions}.
Leave those spaces empty. Do not embed the reference image, any artwork asset,
hidden pictures or a full-slide bitmap in the frame. Keep asset IDs in object
names and a separate guide rather than in the publication figure's visible text.

Export the native PPT frame, a frame preview, and a placement guide listing each
asset ID, every occurrence, and its page coordinates and suggested dimensions.
Inspect native editability and layout. Preserve any existing user-edited file.
```

## P9 — Verify and hand off for manual assembly

```text
Reconcile every required occurrence in the approved reference against the
actual asset files or exact native elements. Check alpha, dimensions, complete
edges, consistent style, native labels and line endpoints. Confirm the main
frame contains no pictures and leaves every artwork location available.

Deliver the exact approved reference, all generated/reused assets, contact sheet,
editable empty frame, frame preview, occurrence manifest, placement guide,
actual prompts and short instructions for manual PowerPoint assembly.
Report what was checked structurally and what was rendered visually.
Verify archive contents and paths. Do not mark planned or missing files complete.
```
