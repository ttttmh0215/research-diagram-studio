# Cartoon scientific style and shared domain adaptation

The visual-language and asset/native-treatment guidance below describes the cartoon branch. For geometric compound shapes, frames and designed arrows, use [geometric-composition.md](geometric-composition.md). The scientific evidence and discipline constraints apply to both branches.

## Visual language

Aim for a readable research figure with cartoon/comic illustration, rather than a page filled with unrelated comic scenes. Useful design patterns include:

| Reference pattern | Transferable visual idea |
|---|---|
| Robot thinking/acting with example crops | One clear character, short hand-lettered headings, aligned example panels |
| Human-loop versus agent-loop composition | Separated conceptual regions, semantic color blocks, local process illustrations |
| Three-panel memory/agent diagram | Strong panel hierarchy, compact symbols, readable inset comparisons and legend |
| Reasoning-system comparison | Comic note boxes, speech/thought shapes, restrained expressive characters |
| Cognitive-memory-action figure | Real photos mixed with cartoons, rounded panels, nested mechanisms |
| Four-part data construction process | Numbered stages, varied pastel cards, bold traceable arrows |
| Segmentation task overview | Consistent example frames, repeated visual vocabulary, supplied task imagery |

These observations are stylistic, not a claim that a particular venue or figure quality has been verified. Do not copy paper names, logos, characters, numerical results or method content from a style reference. A reference's screenshot theme does not determine the final background.

## Composition, color and typography

- Start with a white or very light background for the default publication-oriented style; follow an explicit user preference instead.
- Use visual hierarchy: readable main heading, short section labels, compact body labels. A rounded hand-lettered font can suit headings; longer text needs a clear body font. Keep formulas and scientific symbols precise.
- Choose fonts actually available in the execution environment and supporting the output language. For mixed Chinese/English, avoid missing characters and report substitutions that affect the approved appearance.
- Use a few coherent semantic colors, light panel fills and darker outlines. Different concepts should vary structure, palette and illustration choice, while each concept remains internally consistent.
- Keep subjects recognizable: a meaningful experiment scene, apparatus, cell, model role or engineering device usually communicates more than arbitrary decorative stacks or gears. A robot or person is optional, not mandatory.
- Allow supplied photographs or data subfigures beside cartoon elements. Maintain consistent frames and alignment without changing the content of the evidence.
- Make lines traceable before making them expressive. Avoid arrows through titles, accidental junctions, unclear forks and competing arrowheads. Do not enforce a cycle or comparison layout on a method that has neither.
- For a shared operation or instrument, keep the sample or information paths identifiable; sharing a spectrophotometer, for example, does not mean physically mixing standards, unknowns and blanks. For a separation, retain distinct fraction outlets. Use the paper's relationships rather than treating every fork as the same visual pattern.
- Inspect small instrument screens and analytical insets as well as main panels. Generated microscopy, diffraction spots, heatmaps and fitted/posterior curves can look like evidence even without numbers. Use the actual source when evidence is needed; otherwise choose an unmistakable apparatus or conceptual icon instead of an invented data display.

## Domain decisions

| Domain | Useful cartoon subjects | Content that must remain exact or source-based |
|---|---|---|
| AI, computer science, data systems | Model roles, agents, database/document motifs, retrieval scenes, perception and interaction | Actual architecture connections, algorithm branches, formulas, predictions, masks, benchmark results |
| Physics | Instrument exteriors, sources/detectors, concept particles/waves, experiment scenes | Optical/electrical paths, levels, axes, units, field distributions and measured curves |
| Chemistry and materials | Vessels, apparatus, synthesis stages, explicitly schematic material concepts | Bonds, stereochemistry, reactions, stoichiometry, crystal topology, spectra and microscopy evidence |
| Biology and life sciences | Cells/tissues as schematics, organism illustrations, pipetting/culture steps | Names/sequences, concentrations, sample groups, microscopy/pathology evidence, exact structures and statistics |
| Mechanical, electrical, control and robotics | Devices, robot arms, sensors, operating scenes | Mechanism topology, dimensions, tolerances, circuits, signal/control directions and parameters |
| Civil, energy, environmental and process engineering | Sites, structures, sampling/monitoring scenes, equipment/piping appearance | Spatial dependencies, loads/flows, boundary conditions, measurements and experimental photos |

For another discipline, use the same question: which elements explain the method pictorially, and which encode exact evidence or relationships? Ask for specialist source material only where a missing detail affects correctness. This is a transferable decision rule, not a claim of exhaustive validation in every discipline.

## Asset versus native structure

| Element | Treatment |
|---|---|
| Cartoon subject or coherent vignette | Generate a standalone transparent asset |
| Existing photograph, micrograph, supplied plot or result mask | Reuse its actual source, preserving evidence; list as a supplied asset |
| Plot that must change | Draw from real supplied data with plotting tools; never invent values with image generation |
| Exact molecule, optical/circuit/control topology | Use source-grounded native/vector representation or supplied artwork; no freeform scientific invention |
| Title, panel label, formula, legend label | Native PPT text/equation |
| Background, panel, color block, arrow, decision or connector | Native PPT shape/vector structure |
| Composite inset | Split into native scaffolding and illustration/evidence assets; recurse if necessary |
| Same illustration at multiple positions | One asset, multiple recorded occurrences |

The inventory must account for every occurrence. It does not require every visible object to become a separately generated PNG. Choose a split that preserves independent editing and scientific meaning without producing meaningless fragments.

## Preserving supplied images in concepts

If exact supplied evidence is needed inside a generated concept, keep the original source and a placement ID. Image generation may alter details; do not treat its rendered copy as the authoritative evidence. Keep the actual file for the final asset package, and use a separate layout/placement guide when necessary to show the intended source panel. Generated surroundings may follow the cartoon style while the source image retains its content and meaningful background.
