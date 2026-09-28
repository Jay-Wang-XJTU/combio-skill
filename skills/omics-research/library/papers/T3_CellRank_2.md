# T3 · CellRank 2

## 来源与范围
CellRank 2: unified fate mapping in multiview single-cell data  
Nature Methods · 2024  
目标作者关联：Fabian Theis, Dana Pe'er（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41592-024-02303-9  
原始来源：https://www.nature.com/articles/s41592-024-02303-9

阅读级别：`targeted_full_text`。查阅位置：Main；kernel/estimator 架构；多种方向先验、RealTimeKernel、终态与命运应用 Results。检索日：2026-09-24。

## 原文事实摘取（F）
将转移核构建与 Markov 链分析分离；方向信息可来自多种观测或先验，而非固定依赖 RNA velocity。

输入/输出：输入表达与选定的方向信息；输出状态转移、宏状态、命运概率及关联基因。

定位：Results：kernel/estimator、pseudotime、RealTimeKernel 应用。

## 跨论文归纳的开发决策（S）
先定义方向证据，再比较核；共享下游分析以定位差异来自何处。

## 建议的新项目检查（P；本次未运行）
扰动 root、terminal states、核权重、邻域和缺失终态；检查概率数值与可达性。

## 解释边界与未决事项
命运概率依赖转移模型和终态定义；与命运相关的基因不自动成为因果 driver。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
