# 绘图流程与视觉审查

[English](workflow.md) · [返回首页](../README.zh-CN.md)

![七步科研绘图工作流](images/workflow.zh-CN.png)

1. 读论文，整理节点、连线、标签、公式与证据来源。
2. 生成参考方案，默认两张卡通和两张几何组合；以用户指定的数量和风格为先。
3. 审查示意图：核对论文内容，并独立检查形状、文字与结构合理性，修复明显错误。
4. 展示审查后的方案，询问偏好、错误和修改意见，保留选择分支并记录制作授权。
5. 生成授权范围内的透明素材；需要完整交付时，制作对应风格的留空 PPT。
6. 审查素材：对照确认稿，并检查素材本身。在明暗背景下看实际透明合成效果，检查结构和有意义的数量。重生成后重新审核，再请用户补充错误或修改意见。
7. 用户在 PPT 中组装、另存副本并导出 PDF。

## 两种风格，共用科学主干

卡通分支继续提供原来的科研插画，以及原生 PPT 面板、文字、公式和连线。几何分支增加薄面、堆叠、扇面、矩阵、折叠与梯形组合和特色箭头；平面、轻阴影和少量厚重构件穿插。该分支将组合形状、框架与箭头做成素材，PPT 负责可编辑文字、公式和位置排布。

配色、明暗、饱和度、线宽、厚度和阴影形成层次。用户要“组合造型更丰富”时，需要改变看得见的结构，不能只换颜色或加粗。

## 两次审查分别检查什么

示意图的忠实度对应论文和绘图说明，素材的忠实度对应实际确认版本及指定区域。自身合理性独立检查：形状很像原图，但原图中的层叠、面片、符号本来就有问题，仍然需要修复。

模型必须实际看图并记录具体观察。每个失败项目默认最多做两次针对性修复，尚未解决的明确留待处理。用户反馈在初审之后补充；宿主如果自动显示了生图原始结果，这些也不自动算作通过审查的交付物。

确认稿本身有问题时，也要修复和审查相应参考版本，更新文件与哈希对应；是否需要重新确认，按用户已有授权范围处理。不能只修好素材，却给有缺陷的旧参考图填写“通过”。

## 完整交付与少量试样

完整交付包含确认稿、全部素材及位置、总览、留空 PPT 和预览、坐标与组装说明、实际提示词和审查记录。只想看几个素材时，只生成和审核该子集，不自动做全量清单或 PPT。

可查看 [Bradford 卡通完整实例](../examples/bradford/README.zh-CN.md)和[几何造型试作](../examples/geometric-preview/README.zh-CN.md)，两者验证范围不同。

## 校验方式

新清单使用 schema 2，旧 Bradford 清单继续兼容。脚本检查文件、透明通道、尺寸、位置引用、PPT 结构，以及审查记录与文件哈希的对应关系；它不会自动判断图形是否合理，也不会证明科学内容正确。

```bash
python -m pip install Pillow
python skills/cartoon-research-flowchart/scripts/validate_handoff.py examples/bradford/project.json
python -m unittest discover -s tests -v
```

[提示词模板](../skills/cartoon-research-flowchart/references/prompt-templates.md) · [视觉审查细则](../skills/cartoon-research-flowchart/references/visual-review.md) · [清单格式](../skills/cartoon-research-flowchart/references/manifest-and-delivery.md)
