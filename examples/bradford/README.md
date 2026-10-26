# Bradford protein assay

[简体中文](README.zh-CN.md) · [Repository](../../README.md)

This example shows a complete figure package for the Bradford protein assay, including a reference figure, transparent illustrations, and an editable PowerPoint frame.

**10 unique PNG assets · 14 illustration placements · 2 PPT slides**

## 1. Reference figure

[![Selected Bradford reference concept](reference/Bradford-B-r1.png)](reference/Bradford-B-r1.png)

The conceptual mechanism sits on the left. Standards, unknown, and blank are prepared separately; the shared instrument measures each separately. Blank-corrected standards supply calibration, and the corrected unknown is interpreted using that calibration.

## 2. Receive the transparent illustrations

[![Transparent asset contact sheet](output/transparent-assets.png)](output/transparent-assets.png)

All ten individual PNGs are in [assets/](assets/). A capped vial is reused twice, the pipette three times, and the blue reaction tube twice. A coherent vignette such as the five standard vials is one asset.

## 3. Open the editable frame

[Download the PPTX](output/Bradford-editable-frame.pptx)

[![Artwork-empty editable frame](output/frame-preview.png)](output/frame-preview.png)

Slide 1 contains 73 native objects, including text, panels, formula fragments, arrows, and empty artwork slots. Slide 2 contains 101 native objects and adds placement annotations. Neither slide embeds the illustrations or the full reference image.

## 4. Use the placement guide

[![Numbered positions](output/placement-guide.png)](output/placement-guide.png)

[Placement coordinates](output/placements.csv) · [Assembly instructions](output/assembly.md)

Use the clean slide for assembly. In the selection pane, choose an `ASSET_Axx_Oxx` slot and use its matching PNG as a picture fill, or insert the PNG using the table's coordinates. Keep the instrument's native screen labels above the artwork and the cuvette in front of the instrument. Save an assembled copy.

## Prompts, structure, and checks

- [Concept-generation prompt](prompts/reference-concept.txt)
- [Actual asset prompts](prompts/)
- [Portable asset and occurrence manifest](project.json)
- [File / alpha / PPT validation](verification.json)
- [Native structure source](source/author_framework.mjs): records the frame geometry and labels for a compatible host presentation API. It is optional reference source; opening the supplied PPT needs no authoring library.

The PNG illustrations contain real alpha transparency. The package includes file, image-size, and native PPT structure checks, alongside rendered previews. Protein and dye illustrations serve as conceptual symbols for the assay.

## Scientific source

Marion M. Bradford (1976). *A rapid and sensitive method for the quantitation of microgram quantities of protein utilizing the principle of protein-dye binding.* Analytical Biochemistry 72, 248–254. [DOI](https://doi.org/10.1016/0003-2697(76)90527-3) · [Source PDF](https://hoffman.cm.utexas.edu/courses/bradford_assay.pdf).

The generated example illustrates the assay described in the paper. The original paper PDF and its original figures are not bundled.
