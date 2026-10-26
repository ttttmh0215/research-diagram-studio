<div align="center">

<img src="docs/images/logo.png" width="120" alt="Research Diagram Studio logo">

# Research Diagram Studio

**Turn a paper into a figure you can understand, refine, and assemble.**

English · [简体中文](README.zh-CN.md)

[Download Skill](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/cartoon-research-flowchart.zip) · [Workflow](docs/workflow.md) · [Bradford walkthrough](examples/bradford/README.md) · [Changelog](CHANGELOG.md)

**Current style: cartoon / comic · v0.1.0**

</div>

Research Diagram Studio is an agent skill that helps you make scientific figures. Share your paper and ideas, compare a few designs, and refine the one you like. Once you choose a version, it prepares the transparent illustrations and editable PPT frame for you to assemble.

## What you get

- **Transparent illustrations for PowerPoint!** Each illustration is a separate high-resolution PNG that you can move, resize, and reuse.
- **A complete editable PPT frame!** Edit titles, labels, formulas, color blocks, panels, lines, and arrows. The illustration spaces are already reserved.
- **Your complete reference figure!** Keep the exact design you chose so you can check the layout, colors, and content.
- **A placement guide and coordinate table!** See where each illustration belongs, including every reused occurrence.
- **The actual image prompts and assembly instructions!** Replace illustrations, explore another style, or continue refining the figure later.

**Your final step: put the transparent illustrations into the PPT frame, check the text, layout, and connections, then export your finished PDF for a paper or presentation.**

[Download the complete worked example: assets + PPT + reference](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/bradford-example.zip)


## The visual direction

Cartoon subjects, short labels, deliberate color groups, and a clear scientific story. These complete **paper figures are credited style references**; the [Bradford walkthrough](examples/bradford/README.md) documents the skill's actual outputs.

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

## How it works

[![Research diagram workflow: read, generate, refine, produce assets and frame, assemble and export PDF](docs/images/workflow.en.png)](docs/images/workflow.en.png)

### 1. Work out what the figure needs to say

The agent reads the paper, identifies its problem, main steps, inputs, and outputs, then plans the labels, colors, and illustrations. Include your own sketch or reference images if you already have a direction in mind.

### 2. Compare a few designs and refine your favorite

You usually receive three complete concepts with different layouts, colors, and illustrations. Say “keep B's layout with A's colors,” “replace this object,” or “make it flatter.” The agent follows your feedback and waits for your chosen version before making the assets and PPT.

### 3. Get the illustrations and editable frame

The agent checks the whole figure, including small icons, legends, insets, and repeated objects. It generates separate transparent illustrations and builds the labels, formulas, panels, and arrows as native PPT objects, leaving room for every illustration.

The Bradford example contains **10 unique transparent assets, 14 placements, and a two-slide PPT**. The clean frame and numbered placement guide are separate slides.

<table>
<tr>
<td width="50%"><a href="examples/bradford/output/transparent-assets.png"><img src="examples/bradford/output/transparent-assets.png" alt="Ten transparent Bradford illustration assets"></a><br><b>Transparent illustrations</b><br>Each asset is delivered as its own PNG.</td>
<td width="50%"><a href="examples/bradford/output/frame-preview.png"><img src="examples/bradford/output/frame-preview.png" alt="Native editable PowerPoint frame with illustration spaces left empty"></a><br><b>Editable PPT frame</b><br>Text, panels, formulas, and arrows stay editable.</td>
</tr>
</table>

### 4. Assemble in PowerPoint and export your PDF

Open the PPT frame and insert the illustrations using the placement guide. Resize an icon, enlarge a label, or move an arrow directly in PowerPoint. Check the finished figure, save an assembled copy, and export it as a PDF. You can export a PNG as well when needed.

All files are delivered together so you can return to the figure and keep editing. [See the complete walkthrough →](examples/bradford/README.md)

## Get started

Your agent environment needs image generation with transparent output and a way to create native PPT objects. The skill supplies the workflow and prompts; it uses the capabilities available in the host. It has been exercised in Codex.

1. [Download the Skill ZIP](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/cartoon-research-flowchart.zip).
2. Extract its `cartoon-research-flowchart/` folder into your agent's skills directory. For Codex, use `~/.codex/skills/`.
3. Start a new conversation, attach your paper, and invoke the skill:

```text
Use $cartoon-research-flowchart with this paper.
Generate several cartoon workflow concepts for me to choose from.
After I approve one, deliver every transparent illustration and an editable
PPT frame with the illustration positions left empty. I will assemble it.
```

You can also give `SKILL.md` and its linked references to an agent directly. Image and PPT production still require the relevant tools. See [the detailed workflow and example prompts](docs/workflow.md).

## Scope and development

Current guidance covers AI/computing, physics, chemistry/materials, life sciences, and engineering. Scientific relationships come from the paper; the current style changes their presentation. Supplied evidence images are preserved, and data plots are drawn from data.

| Available now | Planned expansion |
|---|---|
| Cartoon / comic workflow design | More visual styles and style presets |
| Multiple concepts and user-guided refinement | Richer style matching and layout choices |
| Transparent assets + editable PPT structure | Dedicated method and architecture diagram workflows |
| Five-domain concept testing; complete Bradford handoff | More examples, domain templates, and regression cases |

Updates will be published through [Releases](https://github.com/ttttmh0215/research-diagram-studio/releases) and the [Changelog](CHANGELOG.md). Suggestions and examples are welcome in [Issues](https://github.com/ttttmh0215/research-diagram-studio/issues).

## Repository map

```text
skills/cartoon-research-flowchart/  Installable skill, prompts, domain guide, validator
docs/                             Illustrated workflow and reference image credits
examples/bradford/                 Actual assets, editable PPT, manifest, prompts, guides
dist/                             Downloadable Skill ZIP and checksum
```

The skill, original documentation, and original example material use the [MIT license](LICENSE). Third-party paper figures retain their original terms; see [the notices](THIRD_PARTY_NOTICES.md).
