# The complete drawing workflow

[简体中文](workflow.zh-CN.md) · [Home](../README.md)

Share your paper and ideas, compare a few designs, refine your favorite, then use the assets and frame to assemble the figure in PowerPoint.

[![The complete research diagram workflow](images/workflow.en.png)](images/workflow.en.png)

## 1. Read the paper

The agent identifies the problem, main steps, inputs, and outputs, then turns them into a clear figure plan. It also plans the labels, fonts, colors, and illustrations. Include your own sketch, style references, or images if you already have them.

```text
Read this paper and create three cartoon reference figures with different layouts and colors.
Show me the images first. Make the assets and PPT after I choose a version.
```

## 2. Generate a few concepts

You usually receive three complete designs. They explain the same research, with different layouts, colors, and illustration choices. Compare the images and pick the direction closest to what you have in mind.

## 3. Choose and refine

Describe what you like and what you want changed:

```text
Keep B's layout with A's colors. Use fewer illustrations on the right and make the figure flatter.
```

The agent revises your chosen version. When you are happy with it, ask for the transparent assets and PPT frame.

## 4. Make the assets and frame

The agent checks the whole figure and lists every illustration, including small icons, legends, insets, and repeated objects. It creates the illustrations separately and builds the text and structure in an editable PPT.

[![Actual Bradford transparent assets](../examples/bradford/output/transparent-assets.png)](../examples/bradford/output/transparent-assets.png)

This contact sheet shows an actual delivery. Its display background is white; each individual PNG has real transparency. The example has 10 unique assets across 14 placements, with vials and pipettes reused where needed.

[![Native editable PowerPoint frame](../examples/bradford/output/frame-preview.png)](../examples/bradford/output/frame-preview.png)

Edit the headings, labels, formulas, color blocks, lines, and arrows directly. The illustration spaces are reserved, and a separate numbered guide shows where each asset belongs.

## What you get

- **Transparent illustrations for PowerPoint!** Each illustration is a separate high-resolution PNG for insertion, movement, resizing, and reuse.
- **A complete editable PPT frame!** Edit the text and structure, with illustration spaces left empty.
- **Your complete reference figure!** Keep the exact design you selected to compare the overall result.
- **A placement guide and coordinate table!** Find the position and suggested size of every asset.
- **Actual image prompts and assembly instructions!** Keep refining the figure or explore another style later.

[Download the complete example package](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/bradford-example.zip) · [Download the PPT frame directly](../examples/bradford/output/Bradford-editable-frame.pptx)

## 5. Assemble in PowerPoint and export your PDF

Open the clean frame and insert the illustrations using the placement guide. Adjust the text size, illustration positions, arrow directions, and spacing directly in PowerPoint. Check that everything is present, save an assembled copy, and export a PDF for your paper or presentation. Export a PNG as well if needed.

[![Numbered placement guide](../examples/bradford/output/placement-guide.png)](../examples/bradford/output/placement-guide.png)

[Assembly instructions](../examples/bradford/output/assembly.md) · [Coordinates](../examples/bradford/output/placements.csv) · [Complete example](../examples/bradford/README.md)

<details>
<summary>For developers: prompts, domain guidance, and validation</summary>

- [Workflow prompt templates](../skills/cartoon-research-flowchart/references/prompt-templates.md)
- [Style and domain guidance](../skills/cartoon-research-flowchart/references/style-and-domains.md)
- [Asset and delivery manifest](../skills/cartoon-research-flowchart/references/manifest-and-delivery.md)

After installing Pillow, run the read-only checks with Python 3.9 or newer:

```bash
python -m pip install Pillow
python skills/cartoon-research-flowchart/scripts/validate_handoff.py examples/bradford/project.json
```

</details>
