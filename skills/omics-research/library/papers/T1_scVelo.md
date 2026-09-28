# T1 · scVelo

## 来源与范围
Generalizing RNA velocity to transient cell states through dynamical modeling  
Nature Biotechnology · 2020  
目标作者关联：Fabian Theis（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41587-020-0591-3  
原始来源：https://www.nature.com/articles/s41587-020-0591-3

阅读级别：`abstract_plus_official_docs`。查阅位置：论文摘要；官方 Dynamical Modeling 教程的数据准备、动力学拟合与输出说明。检索日：2026-09-24。

## 原文事实摘取（F）
以剪接动力学拟合替代仅依赖稳态的速度估计；官方教程将反应速率和细胞潜在时间共同纳入似然拟合。

输入/输出：输入包含 spliced/unspliced 信息；输出速度、动力学拟合参数、潜在时间等。

定位：论文 Abstract；官方教程 Dynamical Model / Kinetic rate parameters。

## 跨论文归纳的开发决策（S）
先核查方向信息是否存在，再选动态模型；把拟合可信度与流线美观程度分开。

## 建议的新项目检查（P；本次未运行）
检查相图覆盖、拟合残差、关键基因支持、邻域与基因选择敏感性；引入独立方向信息。

## 解释边界与未决事项
潜在时间不自动对应物理时钟；拟合速度不是已观测谱系。原论文完整方法及补充材料未完成核读。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
- https://scvelo.readthedocs.io/en/stable/DynamicalModeling.html

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
