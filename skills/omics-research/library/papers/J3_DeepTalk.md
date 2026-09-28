# J3 · DeepTalk

## 来源与范围
Deciphering cell–cell communication at single-cell resolution for spatial transcriptomics with subgraph-based graph attention network  
Nature Communications · 2024  
目标作者关联：Qinghua Jiang（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41467-024-51329-2  
原始来源：https://www.nature.com/articles/s41467-024-51329-2

阅读级别：`targeted_full_text`。查阅位置：Main；DT-Integration；Methods self/cross attention、subgraph pretraining、link prediction；插补评估。检索日：2026-09-24。

## 原文事实摘取（F）
先做单细胞—空间信息整合，再以子图上下文进行预训练和通讯链接预测。

输入/输出：输入空间数据、scRNA 参考和相关图/先验；输出映射或补全信息及候选通讯。

定位：Methods：Spatial CCC prediction；DT-Integration；gene holdout results。

## 跨论文归纳的开发决策（S）
多模块系统必须为每一级输出建立独立验证；上游定位/插补不确定性需传递到下游。

## 建议的新项目检查（P；本次未运行）
测量与推断坐标分开；基因留出和样本留出分开；扰动映射/邻域并重算互作。

## 解释边界与未决事项
插补精度提升不是通讯准确性证明；从 spots 推断的单细胞位置不能当作直接测量坐标。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
