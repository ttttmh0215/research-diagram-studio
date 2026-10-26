# Assemble the Bradford figure in PowerPoint

[简体中文](assembly.zh-CN.md)

1. Open `Bradford-editable-frame.pptx`. Slide 1 is the clean assembly frame; slide 2 is a placement guide. Save an assembled copy.
2. Compare slide 2 and `placements.csv`. In the selection pane, select an empty slot such as `ASSET_A01_O01`.
3. In Format Shape, use the matching PNG as a picture fill. The slots already match their PNG aspect ratios and sit below the native labels, keeping the display text visible.
4. Alternatively, insert each PNG normally and set its position/size from the CSV. Keep its aspect ratio. Place `TXT_screen_A`, `TXT_screen_595`, and `TXT_screen_nm` in front of the instrument; the A10 cuvette sits in front of A09.
5. Reuse A05 at two input-vial locations, A06 at three reagent-addition locations, and A07 at two blue reaction-tube locations.
6. Check the separate standards, unknown, and blank lanes, then the blank-correction and calibration connections. Adjust spacing and export the finished figure.

Text, panels, formula letters/subscripts, lines, and arrowheads are native editable objects. The illustrations are independent transparent raster PNGs.

The samples are measured separately; the common instrument workflow does not mean sample mixing.
