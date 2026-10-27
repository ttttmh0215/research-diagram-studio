# Workflow and review

[简体中文](workflow.zh-CN.md) · [Home](../README.md)

![Seven-stage workflow](images/workflow.en.png)

1. Read the paper and build the scientific node/edge, label and evidence contract.
2. Generate concepts: normally two cartoon and two geometric, unless the user specifies otherwise.
3. Inspect each concept's fidelity to the paper and intrinsic visual validity. Repair blockers before presenting it as ready.
4. Show reviewed concepts, ask for preference and errors, refine the selected branch, and record actual production authorization.
5. Generate the authorized transparent assets and, when requested, the selected style's empty PPT frame.
6. Inspect assets against the reference AND on their own. Check composited light/dark views, geometry and meaningful counts. Re-review regenerated files; present reviewed samples and ask for user corrections.
7. Assemble manually in PPT, save a copy and export PDF.

## Two styles, one scientific contract

Cartoon subjects and v0.1 native PPT panels/connectors remain available. Geometric mode adds compound planes, stacks, fans, matrices, folded/tapered modules and designed arrows, with flat/light/heavier components mixed. In that mode artwork includes frames and arrows, while the PPT provides editable text/formulas and placement slots.

Palette, lightness, saturation, outline, depth and shadow form a coordinated hierarchy. A request for new constructions must change visible structure, not just recolor the same objects.

## What the reviews decide

For concepts, fidelity means correspondence with the paper/brief. For assets it means correspondence with the exact approved region/construction. Intrinsic validity is independent: a copied impossible stack, malformed face or unreadable symbol still needs repair even if it resembles the reference.

The agent inspects actual files, records concrete observations, repairs blocking defects with at most two targeted attempts per item by default, and leaves unresolved work pending. User feedback follows this initial review. If a host automatically displays raw generation previews, those previews are not yet accepted deliverables.

A defective approved source cannot receive a false pass. Correct and review its version too, rebind files/hashes, and follow the existing authorization scope when deciding whether the corrected reference needs new user approval.

## Full handoff or samples

A full package includes the selected reference, every asset/occurrence, contact sheet, empty frame and preview, coordinates, guides, prompts and review records. Asking for a few samples authorizes only that subset; no full inventory or PPT is needed.

See the [complete Bradford cartoon example](../examples/bradford/README.md) and [geometric appearance trials](../examples/geometric-preview/README.md). These have different validation scopes.

## Validation

New manifests use schema 2; the existing Bradford schema-1 example remains compatible. The script checks files, alpha, sizes, occurrence references, PPT structure, and review-record/file-hash correspondence. It cannot judge images or prove scientific correctness.

```bash
python -m pip install Pillow
python skills/cartoon-research-flowchart/scripts/validate_handoff.py examples/bradford/project.json
python -m unittest discover -s tests -v
```

[Prompt templates](../skills/cartoon-research-flowchart/references/prompt-templates.md) · [Visual review](../skills/cartoon-research-flowchart/references/visual-review.md) · [Manifest schema](../skills/cartoon-research-flowchart/references/manifest-and-delivery.md)
