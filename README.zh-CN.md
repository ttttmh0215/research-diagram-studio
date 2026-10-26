<div align="center">

<img src="docs/images/logo.png" width="120" alt="Research Diagram Studio logo">

# Research Diagram Studio

**把论文变成可以看懂、反复调整、亲手组装的科研图。**

[English](README.md) · 简体中文

[下载 Skill](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/cartoon-research-flowchart.zip) · [完整工作流](docs/workflow.zh-CN.md) · [Bradford 实例](examples/bradford/README.zh-CN.md) · [更新记录](CHANGELOG.md)

**当前风格：卡通漫画 · v0.1.0**

</div>

Research Diagram Studio 是一个帮你画科研图的 Agent Skill。把论文和想法交给它，先看几张方案，选喜欢的继续改。确定后，它会准备好透明素材和可编辑 PPT 框架，让你在 PPT 里完成最后的组装。

## 最终获得

- **PPT 透明背景素材！** 每个图案单独提供高清 PNG，插入 PPT 后可以自由移动、缩放和复用。
- **PPT 完整框架！** 标题、文字、公式、色块、框架、线条和箭头都能编辑，图案的位置已经留好。
- **完整参考示意图！** 保留你最后选定的那张图，方便对照布局、配色和内容。
- **素材定位图和坐标表！** 清楚标出每个图案放在哪里，重复素材也逐处对应。
- **生图提示词和组装说明！** 方便以后换图案、改风格，或继续完善这张图。

**最后一步由你完成：把透明素材放进 PPT 框架，检查文字、布局和连线，调整满意后导出 PDF，放进论文或汇报中。**

[下载完整实测案例：素材＋PPT＋参考图](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/bradford-example.zip)


## 我们希望呈现的视觉方向

有辨识度的卡通主体、简洁文字、有层次的配色，以及一眼能跟下去的科学逻辑。下面展示的是注明出处的**论文风格参考图**；[Bradford 实例](examples/bradford/README.zh-CN.md)展示本 Skill 的实际执行产物。

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

## 完整绘图流程

[![科研绘图完整工作流：读论文、生成方案、选择修改、透明素材与PPT框架、手工组装导出PDF](docs/images/workflow.zh-CN.png)](docs/images/workflow.zh-CN.png)

### 1. 先把论文的主要内容理清楚

模型先读论文，找出研究要解决什么问题、用了哪些关键步骤、输入和输出是什么，再确定图里要写哪些文字、用什么配色、配哪些小图。你有草图或参考图片，也可以一起给它。

### 2. 先看几张图，选喜欢的再改

通常先给你三张完整方案，布局、配色和配图各有不同。你可以直接说“保留 B 的结构，用 A 的颜色”“这里换个图案”“整张图再扁一点”。模型按你的反馈修改，等你确定这一版，再开始制作素材和 PPT。

### 3. 拿到全部素材和可编辑框架

模型会把整张图检查一遍，清点所有图案，包括角落里的小图标、图例和嵌入子图。图案单独生成透明素材；文字、公式、框架和箭头做进 PPT，并保留好每个素材的位置。

Bradford 实测交付了 **10 种透明素材、14 个放置位置和 2 页 PPT**：一页是干净留空框架，一页是编号定位页。

<table>
<tr>
<td width="50%"><a href="examples/bradford/output/transparent-assets.png"><img src="examples/bradford/output/transparent-assets.png" alt="Bradford 案例的十种透明图案素材"></a><br><b>透明图案素材</b><br>每个素材都是可以单独使用的 PNG 文件。</td>
<td width="50%"><a href="examples/bradford/output/frame-preview.png"><img src="examples/bradford/output/frame-preview.png" alt="文字、框架、公式和箭头可编辑的 PPT 留空框架"></a><br><b>可编辑 PPT 框架</b><br>文字、面板、公式、线条和箭头保留为原生对象。</td>
</tr>
</table>

### 4. 在 PPT 里拼好，导出 PDF

打开 PPT 框架，对照定位图把透明素材放进去。觉得字太小、图案太大、箭头不顺，都可以直接在 PPT 里调整。检查完成后，另存一份组装版，再导出 PDF；需要图片时，也可以同时导出 PNG。

整套文件会一起交付，方便你随时接着修改。[查看完整实例 →](examples/bradford/README.zh-CN.md)

## 如何使用

运行环境需要支持透明输出的生图能力，以及创建 PPT 原生对象的工具。Skill 提供工作流和提示词，调用宿主环境中可用的能力；当前已在 Codex 中实测。

1. [下载 Skill ZIP](https://github.com/ttttmh0215/research-diagram-studio/releases/latest/download/cartoon-research-flowchart.zip)。
2. 解压，将 `cartoon-research-flowchart/` 文件夹放入 Agent 的技能目录。Codex 可放入 `~/.codex/skills/`。
3. 新开对话，附上论文并输入：

```text
用 $cartoon-research-flowchart 根据这篇论文制作卡通科研流程图。
先生成几张不同配色、布局和配图的参考方案让我选择。
我确认后，生成每个图案的透明素材，再给我一份图案位置留空、
文字、框架、公式和箭头可编辑的 PPT，我自己组装。
```

也可以把 `SKILL.md` 和其中链接的参考文件直接交给大模型使用；实际生成图片与 PPT 仍需对应工具。[查看详细步骤与示例提示词](docs/workflow.zh-CN.md)。

## 当前范围与后续更新

当前提供 AI 与计算机、物理、化学与材料、生物与生命科学，以及各类工程的领域指导。科学关系来自论文，卡通风格负责视觉表达；已有证据图片保留原内容，数据图根据实际数据绘制。

| 当前已有 | 后续计划 |
|---|---|
| 卡通漫画风格流程图 | 更多风格与可选视觉预设 |
| 多方案生成、用户选择与局部修改 | 更丰富的风格匹配和版式选择 |
| 透明素材＋可编辑 PPT 框架 | 独立的方法图、架构图工作流 |
| 五领域参考图测试、Bradford 完整交付实测 | 更多领域案例、模板和回归测试 |

后续通过 [Releases](https://github.com/ttttmh0215/research-diagram-studio/releases) 和[更新记录](CHANGELOG.md)持续发布。欢迎在 [Issues](https://github.com/ttttmh0215/research-diagram-studio/issues)提出建议或分享使用案例。

## 仓库内容

```text
skills/cartoon-research-flowchart/  可安装 Skill、提示词、领域指南和检查脚本
docs/                             图文工作流、参考图及出处
examples/bradford/                 真实素材、PPT、清单、提示词和组装说明
dist/                             Skill 下载包和校验值
```

Skill、原创文档和原创示例材料采用 [MIT 许可](LICENSE)。第三方论文参考图保留原作者及出版方的权利和原有条款，详见[来源说明](THIRD_PARTY_NOTICES.md)。
