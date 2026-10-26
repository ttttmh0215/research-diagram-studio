# Bradford 蛋白定量实例

[English](README.md) · [返回仓库](../../README.zh-CN.md)

本例展示 Bradford 蛋白定量图的完整交付内容，包括参考示意图、透明图案素材和可编辑 PowerPoint 框架。

**10 种独立 PNG 素材 · 14 个图案位置 · 2 页 PPT**

## 1. 参考示意图

[![选定的 Bradford 参考图](reference/Bradford-B-r1.png)](reference/Bradford-B-r1.png)

左侧展示概念机制。标准品、未知样品和空白分别制备，再分别使用同一台仪器测量。空白校正后的标准品数据用于校准，未知样品的校正信号结合校准信息得到蛋白量。

## 2. 领取全部透明素材

[![十种透明素材总览](output/transparent-assets.png)](output/transparent-assets.png)

10 张独立 PNG 均位于 [assets/](assets/)。输入瓶复用两处，移液器复用三处，蓝色反应管复用两处；五个标准品瓶组成的完整场景计为一张素材。

## 3. 打开可编辑框架

[下载 PPTX](output/Bradford-editable-frame.pptx)

[![图案位置留空的 PPT 框架](output/frame-preview.png)](output/frame-preview.png)

第1页包含73个原生对象，包括文字、色块、公式片段、箭头和空白素材槽位。第2页包含101个原生对象，增加了定位标记。两页都没有把图案或整张参考图嵌进去。

## 4. 对照位置完成组装

[![编号定位页](output/placement-guide.png)](output/placement-guide.png)

[坐标表](output/placements.csv) · [组装说明](output/assembly.zh-CN.md)

用第1页完成组装。在选择窗格中找到 `ASSET_Axx_Oxx`，将对应 PNG 设为该形状的图片填充；也可以按表格坐标直接插入。仪器屏幕的原生文字放在图案上层，比色皿位于仪器前方。最后另存组装副本。

## 实际提示词、源文件和检查记录

- [参考图生成提示词](prompts/reference-concept.txt)
- [实际素材提示词](prompts/)
- [可移植素材与位置清单](project.json)
- [文件、透明度与 PPT 结构检查](verification.json)
- [框架绘制源文件](source/author_framework.mjs)：记录原生几何与文字，需要兼容的宿主演示文稿 API。它作为可选参考源码提供，直接打开 PPT 无须配置绘制库。

PNG 图案具有真实透明背景。交付文件包含素材尺寸与原生 PPT 结构检查记录，并提供框架及定位页预览。蛋白与染料图案用于解释实验原理。

## 科学内容来源

Marion M. Bradford（1976）.*A rapid and sensitive method for the quantitation of microgram quantities of protein utilizing the principle of protein-dye binding.* Analytical Biochemistry 72, 248–254。[DOI](https://doi.org/10.1016/0003-2697(76)90527-3) · [原文 PDF](https://hoffman.cm.utexas.edu/courses/bradford_assay.pdf)。

本例根据论文描述重新生成解释性示意图；公开包不附原论文 PDF 和原论文图片。
