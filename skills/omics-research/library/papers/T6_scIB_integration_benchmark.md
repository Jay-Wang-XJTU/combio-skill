# T6 · scIB integration benchmark

## 来源与范围
Benchmarking atlas-level data integration in single-cell genomics  
Nature Methods · 2021 在线；2022 卷期  
目标作者关联：Fabian Theis（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41592-021-01336-8  
原始来源：https://www.nature.com/articles/s41592-021-01336-8

阅读级别：`targeted_full_text`。查阅位置：Main/Results：评价体系、输出类型、预处理、scRNA/scATAC、多目标权衡。检索日：2026-09-24。

## 原文事实摘取（F）
整合评价同时关注批次去除与生物学保留，并区分 graph、embedding、corrected matrix 等输出。

输入/输出：输入多批次数据、注释和方法输出；输出多维评价而非单一混合分数。

定位：Main：evaluation metrics、preprocessing、output categories。

## 跨论文归纳的开发决策（S）
评价器必须与输出和任务兼容；保留细胞类型之外的状态变化。

## 建议的新项目检查（P；本次未运行）
分别报告 batch/biology；披露标签使用、调参资源、预处理与失败；跨数据集检查取舍。

## 解释边界与未决事项
论文中的指标权重和当时排序不是永久标准，也不能直接成为空间肿瘤任务的普适评分。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
