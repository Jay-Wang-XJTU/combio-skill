# C2 · stKeep

## 来源与范围
Dissecting tumor microenvironment from spatially resolved transcriptomics data by heterogeneous graph learning  
Nature Communications · 2024  
目标作者关联：Luonan Chen（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41467-024-49171-7  
原始来源：https://www.nature.com/articles/s41467-024-49171-7

阅读级别：`targeted_full_text`。查阅位置：Main；heterogeneous graphs；cell/gene/communication modules；输入信息说明。检索日：2026-09-24。

## 原文事实摘取（F）
异构图结合细胞、基因与区域等信息，分析细胞状态、基因模块及通讯；输入包含病理区域和相关先验。

输入/输出：输入表达、空间/组织信息及知识先验；输出多层次表征与候选互作。

定位：Methods：heterogeneous graph construction；三模块描述。

## 跨论文归纳的开发决策（S）
图节点和边类型需逐一赋予观测或先验语义；把额外信息计入方法贡献。

## 建议的新项目检查（P；本次未运行）
分别去除组织区域、图像和先验；避免用训练使用的区域标签独立证明发现。

## 解释边界与未决事项
监督/先验信息不能隐去；注意力和图关联仅提供计算解释，不直接证明通讯机制。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
