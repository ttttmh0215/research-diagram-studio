<div align="center">

<img src="docs/images/logo.png" width="120" alt="Research Diagram Studio 标识">

# Research Diagram Studio

**把论文变成可以审阅、修改、亲手组装的科研图。**

[English](README.md) · 简体中文

[下载 Skill](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/research-diagram-studio.zip) · [两种风格](#两种绘图风格) · [绘图流程](#从论文到科研图) · [交付内容](#交付包里有什么) · [安装使用](#安装与第一次使用)

**Agent Skill · 科研流程图、方法图与架构图 · v0.2.0**

</div>

Research Diagram Studio 是一个**科研绘图 Agent Skill**。你提供论文、方法说明或研究想法，它帮助整理科学主干、生成视觉方案、根据反馈修改，再准备独立透明素材和可编辑的 PowerPoint 组装框架。

你来选择视觉方向，并在 PPT 中完成最后调整。Skill 在示意图和素材生成后分别进行视觉审查，帮助提前发现内容和造型问题。当前版本提供卡通漫画与几何组合两种风格，共用同一套绘图流程。

## 两种绘图风格

根据图里要解释的内容选择画风。两种风格都以同一份论文信息为基础，保留输入、输出、模块、条件、分支和连接关系。

| 风格 | 主要视觉特点 | 适合表达的内容 |
|---|---|---|
| **卡通漫画** | 可识别的科研主体、完整小场景、插画叙事和清楚的面板层次 | 实验步骤、原理机制、需要具体主体帮助理解的过程 |
| **几何组合** | 重叠薄面、堆叠、扇面、矩阵、折叠模块和特色箭头，配合色彩与轻重变化 | 模型架构、多分支方法、结构关系较多的技术流程 |

### 卡通漫画

卡通图把科研主体与简洁标签、分区和连线结合起来。内容需要时，也可以保留真实照片或科学子图，与插画共同排版。

下面是 Bradford 实例中**选定的完整参考示意图**，用于确定整体布局和视觉效果。后面会接着展示由它制作的独立素材与可编辑框架。

[![Bradford 实例选定的卡通参考示意图](examples/bradford/reference/Bradford-B-r1.png)](examples/bradford/reference/Bradford-B-r1.png)

### 几何组合

这一类图由简单形状组合出结构：错位矩形、薄片、矩阵块、梯形、复合模块和有特色的连线。可以穿插平面、轻阴影和少量厚重构件，同时安排配色、明暗、线宽和箭头样式，让画面既有层次，也能顺着主流程阅读。

下面的**造型试样**展示三种已有构件：层叠特征片、蓝色与珊瑚色组合模块，以及渐变弧形箭头。它们用于说明素材外观，目前还不是一整套经过科学审查的论文图交付。

[![几何造型试样：层叠薄片、组合模块和弧形箭头](examples/geometric-preview/preview.png)](examples/geometric-preview/README.zh-CN.md)

后续新增风格仍可放进同一个 Skill。下面工作流宣传图采用卡通插画，不限制实际生成科研图时使用哪种画风。

## 从论文到科研图

整个过程先明确科学内容，再选择和修改设计，最后制作可供手工组装的材料。

[![包含示意图审查与素材审查的七步科研绘图流程](docs/images/workflow.zh-CN.png)](docs/images/workflow.zh-CN.png)

1. **读论文，理思路。** 提取研究问题、输入与输出、关键模块、准确标签和公式，以及图中必须保留的关系。
2. **生成参考方案。** 默认两张卡通、两张几何组合；也可以指定某一种风格或其他数量。
3. **审查示意图。** 检查科学内容、文字、连线和图形结构，修复明显错误后，再把审查后的方案交给你选择。
4. **选择与修改。** 选定版本，说明想保留和调整的地方，例如采用一张的布局、另一张的配色。
5. **生成素材与框架。** 你确认制作后，根据选定设计生成透明素材，以及相应的留空 PPT。
6. **审查生成素材。** 对照确认稿检查，同时判断素材本身是否合理；失败的修复或重新生成，再请你补充错误或修改意见。
7. **组装与导出。** 在 PPT 插入素材，调整文字和位置，另存组装副本，最后导出 PDF。

两次审查都是模型先检查，再请你指出剩余错误或想修改的地方。重点分别是：

- **是否忠实？** 示意图是否符合论文，素材是否符合选定设计。
- **本身是否合理？** 面片、堆叠、数量、符号、文字和箭头关系是否清楚、连贯。照着有问题的参考图生成得很像，仍然需要修正。

透明通道、尺寸和文件检查辅助看图，不能代替视觉判断。如果你只想先看几个素材，Skill 就先完成这个子集，收到进一步指示后再制作剩余素材或 PPT。

## 交付包里有什么

完整交付提供的是便于组装、以后也能继续修改的一套材料：

| 交付内容 | 用来做什么 |
|---|---|
| **选定版本的参考图** | 对照布局、配色和整体视觉效果 |
| **独立透明 PNG 与素材总览** | 分别移动、缩放和复用图案 |
| **可编辑的留空 PPT 与预览** | 调整文字、公式和与风格匹配的排布 |
| **定位图与坐标表** | 对应每个素材的位置和建议大小 |
| **实际生图提示词与组装说明** | 重新生成某个素材，或接着修改这张图 |
| **视觉审查记录** | 了解检查了哪些文件，以及还有哪些问题待解决 |

下面用 Bradford 实例展示这套交付：**10 种独立素材、14 个放置位置、2 页 PPT**，分别是干净框架和编号定位页。

### 1. 独立透明素材

素材总览方便一次看清全部图案，每个图案也单独提供透明 PNG。同一张图案可以放在多个位置，不需要每处都重新生成。

[![Bradford 实例的十种独立透明素材总览](examples/bradford/output/transparent-assets.png)](examples/bradford/output/transparent-assets.png)

下面三个实际文件展示素材如何拆分：完整的试管小场景、原理示意图案，以及仪器。它们与文字分开，便于以后在 PPT 中修改标签。

<table>
<tr>
<td width="33%" valign="top"><a href="examples/bradford/assets/A04_five_standard_vials.png"><img src="examples/bradford/assets/A04_five_standard_vials.png" width="220" alt="五个标准品瓶组成的独立透明素材"></a><br><b>完整小场景</b><br>一组试管作为一个素材整体移动。</td>
<td width="33%" valign="top"><a href="examples/bradford/assets/A03_blue_protein_dye_complex.png"><img src="examples/bradford/assets/A03_blue_protein_dye_complex.png" width="220" alt="独立透明的蛋白与染料结合概念插画"></a><br><b>原理示意图案</b><br>插画与标签、公式分开。</td>
<td width="33%" valign="top"><a href="examples/bradford/assets/A09_spectrophotometer.png"><img src="examples/bradford/assets/A09_spectrophotometer.png" width="220" alt="独立透明的分光光度计插画"></a><br><b>可复用仪器</b><br>放进框架中的对应位置。</td>
</tr>
</table>

### 2. 留空但可编辑的 PPT 框架

下面留白的位置是给图案预留的。在卡通分支里，标签、公式片段、面板和流程箭头都是 PPT 原生对象，插画由你另行放入。

[![图案位置留空的 Bradford 原生可编辑 PPT 框架](examples/bradford/output/frame-preview.png)](examples/bradford/output/frame-preview.png)

不同风格采用相应的框架处理方式：

| 分支 | 作为透明素材交付 | 保留在 PPT 中 |
|---|---|---|
| **卡通** | 插画及实际需要复用的图片 | 原生文字、公式、面板和连线，以及留空的图案位置 |
| **几何组合** | 组合形状、框架和特色箭头 | 可编辑文字、公式、整体排布，以及留空的素材位置 |

PNG 可以整体移动和缩放，但内部的每个子形状不会自动成为 PPT 原生对象。

### 3. 定位与手工组装

编号页告诉你每个素材放在哪里，也标出同一素材的重复使用位置。坐标表提供位置和建议大小，组装说明则解释如何插入、对齐和叠放素材。

[![将素材编号对应到放置位置的 Bradford 定位页](examples/bradford/output/placement-guide.png)](examples/bradford/output/placement-guide.png)

打开干净框架，插入对应素材，保持纵横比，检查文字与连线的位置关系；完成后另存一份组装副本，再导出 PDF。

[下载 PPT](examples/bradford/output/Bradford-editable-frame.pptx) · [坐标表](examples/bradford/output/placements.csv) · [组装说明](examples/bradford/output/assembly.zh-CN.md) · [完整案例 ZIP](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/bradford-example.zip)

## 安装与第一次使用

Agent 环境需要具备透明生图能力；完整交付 PPT 时，还需要演示文稿制作工具。Skill 提供流程和提示词，调用宿主中实际可用的能力。

1. 下载 [Skill ZIP](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/research-diagram-studio.zip)。
2. 解压，把 `cartoon-research-flowchart/` 放进技能目录，例如 `~/.codex/skills/`。
3. 新开对话，附上论文并输入：

```text
用 $cartoon-research-flowchart 根据这篇论文制作科研图。
先生成两张卡通、两张几何组合方案，经过视觉审查后给我选择，
也问问我有没有发现错误。
我确认制作后，再生成经过审查的透明素材和对应的留空 PPT，
由我最后组装。
```

界面显示名为 **Research Diagram Studio**，原调用方式以及旧的 [cartoon-research-flowchart.zip](dist/cartoon-research-flowchart.zip) 下载名保持兼容。

<details>
<summary>后续可以这样提出修改或试做要求</summary>

```text
保留 G1 的结构，采用 C2 的配色，箭头再轻一点。
先把修改后的完整参考图给我看，再制作素材。
```

```text
就用已经选定的第一版，先生成三个代表性透明素材，
暂时不做全量素材和 PPT。
```

```text
这篇论文只看几何组合方案。
让平面、带轻阴影的薄面和少量立体模块穿插。
```

</details>

[详细工作流](docs/workflow.zh-CN.md) · [Skill 正文](skills/cartoon-research-flowchart/SKILL.md) · [提示词模板](skills/cartoon-research-flowchart/references/prompt-templates.md)

## 论文风格参考

下面四张**有明确出处的论文参考图**，展示插画主体、真实照片与卡通混排、多分区构图和重复图案等视觉处理。它们用于学习风格；前面各节展示的才是本 Skill 的实际示例材料。

[![ThinkAct：卡通主体与推理、执行过程的组合](docs/images/references/thinkact.jpg)](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7749f9c0d5ff109231be21e910a3ced2-Abstract-Conference.html)

*ThinkAct — Huang 等，NeurIPS 2025。紧凑的横向叙事，将卡通角色、推理文本与真实任务画面组合起来。*

<table>
<tr>
<td width="50%"><a href="https://openreview.net/forum?id=Ws8swqL5ob"><img src="docs/images/references/photoagent.jpg" alt="PhotoAgent：人工操作与智能体工作流对比参考图"></a><br><b>PhotoAgent</b> · Yao 等<br>对比式叙事、循环结构、人物与图标的配合。</td>
<td width="50%"><a href="https://openreview.net/forum?id=54U3XHf7qq"><img src="docs/images/references/memoryvla.jpg" alt="MemoryVLA：认知机制与机器人模型架构参考图"></a><br><b>MemoryVLA</b> · Shi 等<br>卡通机制、模型模块与真实图像的混合排版。</td>
</tr>
</table>

[![多智能体研究三栏参考图：记忆、交互与研究发现](docs/images/references/troublemaker.jpg)](https://aclanthology.org/2025.acl-long.859/)

*A Troublemaker with Contagious Jailbreak Makes Chaos in Honest Towns — Men 等，ACL 2025。三个相互联系的分区、重复角色与统一图例。*

参考图均出自公开论文，仅供学习与风格参考；如有版权或署名问题，请通过 [Issue](https://github.com/ttttmh0215/research-diagram-studio/issues) 联系仓库作者删除。

[完整参考说明](docs/style-references.md) · [来源记录](docs/reference-sources.json) · [第三方素材说明](THIRD_PARTY_NOTICES.md)

## 当前范围与后续更新

| 当前已有 | 示例进展 |
|---|---|
| 卡通流程图与原生组装框架 | [Bradford 完整交付](examples/bradford/README.zh-CN.md)来自 v0.1，保留其原始材料与检查记录 |
| 几何方案、组合素材和文字定位框架指导 | 当前提供[三个造型试样](examples/geometric-preview/README.zh-CN.md)，后续补充完整科学图交付案例 |
| 示意图、素材两次视觉审查 | v0.2 已加入，配套具体文件的审查记录与结构校验 |
| 少量素材试做 | 可先完成指定子集，不自动制作全量素材或 PPT |

当前领域指导覆盖计算机、物理、化学与材料、生命科学和工程。科学关系来自论文；已有证据图片保留真实内容，修改数据图需要实际数据。后续继续增加视觉风格、构图预设和更多领域的完整案例。

## 仓库内容与出处

```text
skills/cartoon-research-flowchart/  Agent Skill、风格指南、提示词和校验脚本
docs/                             中英文工作流、项目标识和参考出处
examples/                         完整交付及明确标注的试作
tests/                            审查记录与兼容性检查
dist/                             可安装 Skill ZIP 及 SHA256 校验值
```

[版本发布](https://github.com/ttttmh0215/research-diagram-studio/releases) · [更新记录](CHANGELOG.md) · [反馈建议](https://github.com/ttttmh0215/research-diagram-studio/issues) · [参与贡献](CONTRIBUTING.md)

原创代码、Skill 说明和原创示例采用 [MIT 许可](LICENSE)。第三方论文参考图保留原作者与出版方的权利及条款。
