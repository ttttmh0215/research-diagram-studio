<div align="center">

<img src="docs/images/logo.png" width="120" alt="Research Diagram Studio logo">

# Research Diagram Studio

**Turn a research paper into a diagram you can review, refine and assemble.**

English · [简体中文](README.zh-CN.md)

[Download Skill](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/research-diagram-studio.zip) · [Styles](#two-visual-styles) · [Workflow](#from-paper-to-diagram) · [Deliverables](#inside-the-delivery-package) · [Get started](#installation-and-first-use)

**Agent Skill · Scientific flowcharts, method diagrams and architecture figures · v0.2.0**

</div>

Research Diagram Studio is an **Agent Skill** for turning a paper, method description or research idea into scientific figure materials. It helps organize the scientific story, proposes visual concepts, follows your revisions, and prepares transparent assets with an editable PowerPoint assembly frame.

You choose the design and make the final adjustments in PPT. The Skill supports that process with two visual-review stages: one for complete reference concepts and one for the generated assets. The current version offers cartoon/comic and geometric-composition styles within the same workflow.

## Two visual styles

Choose the visual language that suits the explanation. Both styles start from the same paper-specific content: inputs, outputs, modules, conditions, branches and connections.

| Style | What it emphasizes | Useful for |
|---|---|---|
| **Cartoon / comic** | Recognizable scientific subjects, coherent scenes, expressive illustrations and clear panel hierarchy | Experimental procedures, conceptual mechanisms and illustrated explanations |
| **Geometric composition** | Overlapping planes, stacks, fans, matrices, folded modules and designed arrows, with varied color, depth and visual weight | Model architectures, multi-branch methods and structured technical processes |

### Cartoon / comic

Cartoon figures combine scientific subjects with readable labels, panels and connections. Supplied photographs or scientific subfigures can be used alongside the illustrations when the content calls for them.

The image below is the **selected reference concept** from the Bradford example. It shows the intended composition and appearance; the separate assets and editable frame used for manual assembly are shown later.

[![Selected Bradford reference concept, showing an illustrated scientific procedure](examples/bradford/reference/Bradford-B-r1.png)](examples/bradford/reference/Bradford-B-r1.png)

### Geometric composition

This style builds visual structure from simple shapes: offset rectangles, thin feature sheets, matrix tiles, tapered plates, compound modules and distinctive connectors. Flat faces, light shadows and a few deeper objects can be mixed to give the figure a clear rhythm. Palette, contrast, line weight and arrow treatment are designed together.

The following **appearance trials** show three existing constructions: layered feature sheets, a blue–coral–blue compound module and a curved gradient arrow. They demonstrate asset appearance, not a complete scientifically validated paper-figure handoff.

[![Geometric appearance trials: layered sheets, a compound module and a curved connector](examples/geometric-preview/preview.png)](examples/geometric-preview/README.md)

More visual styles can be added to the same Skill. The cartoon artwork used in the workflow illustration below does not restrict the style of the figures it produces.

## From paper to diagram

The process moves from scientific planning to design selection, then to materials for manual assembly.

[![Seven-stage workflow with concept review and asset review](docs/images/workflow.en.png)](docs/images/workflow.en.png)

1. **Read and plan.** Identify the research problem, inputs, outputs, essential modules, exact labels and formulas, and the relationships the figure must preserve.
2. **Generate reference concepts.** By default, produce two cartoon and two geometric proposals. You can request a particular style or another count.
3. **Review the concepts.** Inspect scientific content, text, connections and visual construction. Repair blocking errors before presenting the reviewed candidates.
4. **Choose and refine.** Pick a version and describe what to keep or change. You can combine preferences, such as one concept's layout with another's palette.
5. **Make assets and frame.** After you authorize production, create the selected design's transparent assets and the appropriate empty PPT frame.
6. **Review the assets.** Compare each asset with its reference and check whether its construction makes sense on its own. Repair or regenerate failures, then ask for your corrections.
7. **Assemble and export.** Insert the assets into PPT, adjust text and placement, save an assembled copy and export the final PDF.

The agent reviews first, then asks you to point out remaining errors or changes. The two review questions are:

- **Is it faithful?** Does the concept follow the paper, and does each asset follow the selected design?
- **Is it reasonable in itself?** Are the faces, stacks, counts, symbols, text and arrow relationships coherent? A faithful copy of a malformed reference still needs correction.

Transparent-background and file checks support this review; they do not replace looking at the image. If you ask to see only a few sample assets, the Skill produces that subset and waits for further instructions before making the remaining batch or PPT.

## Inside the delivery package

A full handoff gives you the materials needed to assemble and keep editing the figure:

| Material | How you use it |
|---|---|
| **Selected reference figure** | Follow the approved layout, colors and overall appearance |
| **Independent transparent PNGs and contact sheet** | Move, resize and reuse the artwork |
| **Empty editable PPT frame and preview** | Work with the text, formulas and style-specific layout |
| **Placement guide and coordinate table** | Match each asset to its intended position and size |
| **Actual prompts and assembly instructions** | Regenerate an asset or continue the figure later |
| **Visual-review records** | See which files were inspected and which issues remain unresolved |

The Bradford example below illustrates this handoff with **10 unique assets, 14 placements and two PPT slides**: a clean assembly frame and a numbered placement page.

### 1. Transparent assets

The contact sheet makes the whole asset set easy to inspect. Every illustration is also supplied as its own transparent PNG. Identical artwork can be reused at several positions.

[![Contact sheet of the ten independent Bradford illustration assets](examples/bradford/output/transparent-assets.png)](examples/bradford/output/transparent-assets.png)

These three files show the intended level of separation: a coherent vial scene, a conceptual protein–dye illustration and an instrument. Their wording remains separate so it can be edited in PPT.

<table>
<tr>
<td width="33%" valign="top"><a href="examples/bradford/assets/A04_five_standard_vials.png"><img src="examples/bradford/assets/A04_five_standard_vials.png" width="220" alt="Independent transparent asset containing five standard vials"></a><br><b>A complete small scene</b><br>The vial group moves as one asset.</td>
<td width="33%" valign="top"><a href="examples/bradford/assets/A03_blue_protein_dye_complex.png"><img src="examples/bradford/assets/A03_blue_protein_dye_complex.png" width="220" alt="Independent transparent conceptual protein–dye illustration"></a><br><b>A conceptual illustration</b><br>Artwork is separate from labels and formulas.</td>
<td width="33%" valign="top"><a href="examples/bradford/assets/A09_spectrophotometer.png"><img src="examples/bradford/assets/A09_spectrophotometer.png" width="220" alt="Independent transparent spectrophotometer illustration"></a><br><b>A reusable instrument</b><br>Place it in the matching assembly slot.</td>
</tr>
</table>

### 2. An editable, artwork-empty frame

The spaces below are intentionally empty. In the cartoon branch, labels, equation components, panels and workflow arrows are native PPT objects; the illustrations are inserted separately.

[![Bradford native PowerPoint frame with the artwork positions left empty](examples/bradford/output/frame-preview.png)](examples/bradford/output/frame-preview.png)

The frame treatment follows the selected style:

| Branch | Delivered as transparent artwork | Kept in the PPT frame |
|---|---|---|
| **Cartoon** | Illustrations and supplied picture assets | Native text, formulas, panels and connectors; empty artwork positions |
| **Geometric** | Compound shapes, frames and designed arrows | Editable text and formulas, overall layout and empty asset positions |

PNG assets can be moved and resized as whole objects. Their internal subshapes are not automatically native editable PPT geometry.

### 3. Placement and manual assembly

The numbered page tells you where each asset belongs, including repeated uses of the same PNG. The coordinate table provides positions and suggested sizes; the assembly guide explains how to insert and align the files.

[![Numbered Bradford placement page linking assets to their intended positions](examples/bradford/output/placement-guide.png)](examples/bradford/output/placement-guide.png)

Open the clean frame, insert the matching assets, keep their aspect ratios, check text and connector alignment, and save an assembled copy before exporting PDF.

[Download the PPT](examples/bradford/output/Bradford-editable-frame.pptx) · [Coordinate table](examples/bradford/output/placements.csv) · [Assembly guide](examples/bradford/output/assembly.md) · [Complete example ZIP](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/bradford-example.zip)

## Installation and first use

Your agent environment needs image generation with transparent output. Producing a full PPT handoff also needs a presentation-authoring tool. The Skill provides the instructions and prompts and uses the host's available capabilities.

1. Download the [Skill ZIP](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/research-diagram-studio.zip).
2. Extract `cartoon-research-flowchart/` into your skills directory, such as `~/.codex/skills/`.
3. Start a new chat, attach your paper and enter:

```text
Use $cartoon-research-flowchart with this paper.
First show two cartoon and two geometric concepts after visual review.
Ask which one I prefer and whether I see any errors.
After I approve production, make the reviewed transparent assets and
the matching empty PPT frame. I will assemble the final figure.
```

The display name is **Research Diagram Studio**. The existing invocation and the legacy [cartoon-research-flowchart.zip](dist/cartoon-research-flowchart.zip) remain compatible.

<details>
<summary>Useful follow-up requests</summary>

```text
Keep G1's layout, use C2's palette, and make the arrows lighter.
Show the revised reference before making assets.
```

```text
Use the selected first version. Generate three representative
transparent assets only; do not make the full batch or PPT yet.
```

```text
For this paper, show only geometric concepts.
Mix flat faces, lightly shadowed planes and a few deeper modules.
```

</details>

[Detailed workflow](docs/workflow.md) · [Skill instructions](skills/cartoon-research-flowchart/SKILL.md) · [Prompt templates](skills/cartoon-research-flowchart/references/prompt-templates.md)

## Paper-style inspiration

The following **credited figures from published papers** show visual ideas such as illustrated subjects, mixed photographs and cartoons, multi-panel composition and recurring motifs. They are style references. The Skill's own example materials are shown in the earlier sections.

[![ThinkAct — cartoon reasoning and action overview](docs/images/references/thinkact.jpg)](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7749f9c0d5ff109231be21e910a3ced2-Abstract-Conference.html)

*ThinkAct — Huang et al., NeurIPS 2025. A compact sequence mixing a cartoon character, reasoning panels, and real task images.*

<table>
<tr>
<td width="50%"><a href="https://openreview.net/forum?id=Ws8swqL5ob"><img src="docs/images/references/photoagent.jpg" alt="PhotoAgent: people-loop and agent-loop visual reference"></a><br><b>PhotoAgent</b> · Yao et al.<br>Visual comparison and a central iterative workflow.</td>
<td width="50%"><a href="https://openreview.net/forum?id=54U3XHf7qq"><img src="docs/images/references/memoryvla.jpg" alt="MemoryVLA: cartoon cognition and robotic architecture reference"></a><br><b>MemoryVLA</b> · Shi et al.<br>Cartoon mechanisms, model modules, and real images.</td>
</tr>
</table>

[![Multi-agent cartoon reference — memory, interaction, and findings](docs/images/references/troublemaker.jpg)](https://aclanthology.org/2025.acl-long.859/)

*A Troublemaker with Contagious Jailbreak Makes Chaos in Honest Towns — Men et al., ACL 2025. Three connected panels with reusable characters and a shared legend.*

Reference figures are sourced from publicly available papers for study and visual inspiration. For copyright or attribution concerns, please contact the repository author through an [issue](https://github.com/ttttmh0215/research-diagram-studio/issues) for removal.

[All reference notes](docs/style-references.md) · [Source records](docs/reference-sources.json) · [Third-party notices](THIRD_PARTY_NOTICES.md)

## Current scope and next steps

| Available now | Example status |
|---|---|
| Cartoon/comic workflow and native assembly frame | [Complete Bradford handoff](examples/bradford/README.md), created with v0.1 and retaining its original records |
| Geometric concepts, compound assets and text-placement frame guidance | [Three appearance trials](examples/geometric-preview/README.md); a complete scientific-figure handoff is still to be added |
| Concept and asset visual-review gates | Included in v0.2, with file-bound review records and structural validation |
| Sample-only production | Produce a requested subset without automatically starting a full batch or PPT |

Domain guidance currently covers computing, physics, chemistry/materials, life sciences and engineering. Scientific relationships come from the source paper; supplied evidence is preserved, and changed data plots require real data. Future updates can add visual styles, composition presets and complete examples from more fields.

## Repository and credits

```text
skills/cartoon-research-flowchart/  The Agent Skill, style guides, prompts and validator
docs/                             Bilingual workflow, branding and reference credits
examples/                         Complete handoffs and clearly labelled trials
tests/                            Review-record and compatibility checks
dist/                             Installable Skill ZIPs and SHA256 checksums
```

[Releases](https://github.com/ttttmh0215/research-diagram-studio/releases) · [Changelog](CHANGELOG.md) · [Issues](https://github.com/ttttmh0215/research-diagram-studio/issues) · [Contributing](CONTRIBUTING.md)

Original code, skill instructions and original example material use the [MIT license](LICENSE). Third-party paper figures retain their original rights and terms.
