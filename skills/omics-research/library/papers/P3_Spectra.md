# P3 · Spectra

## 来源与范围
Supervised discovery of interpretable gene programs from single-cell data  
Nature Biotechnology · 2023 在线；2024 卷期  
目标作者关联：Dana Pe'er（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41587-023-01940-3  
原始来源：https://www.nature.com/articles/s41587-023-01940-3

阅读级别：`targeted_full_text`。查阅位置：Main；Results 前两部分；factor importance/information 等 Methods。检索日：2026-09-24。

## 原文事实摘取（F）
以细胞类型信息和基因知识图约束因子分解，同时允许共享、特异及新程序；以已知刺激数据检查程序响应。

输入/输出：输入标准化表达、细胞类型和 gene sets/knowledge graph；输出 cell scores 与 gene loadings。

定位：Fig. 1 刺激验证；Fig. 2 gene holdout；Methods factor metrics。

## 跨论文归纳的开发决策（S）
将身份差异、功能状态和先验支持分开建模；为先验以外的变化留下表达空间。

## 建议的新项目检查（P；本次未运行）
先验基因留出；program overlap 审计；独立刺激/样本验证；区分总体贡献和类型内信息。

## 解释边界与未决事项
输入标签和 gene sets 是额外信息，比较时必须披露；与输入基因集重叠不能独立证明机制。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
