# P1 · Palantir

## 来源与范围
Characterization of cell fate probabilities in single-cell data with Palantir  
Nature Biotechnology · 2019  
目标作者关联：Dana Pe'er（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41587-019-0068-4  
原始来源：https://www.nature.com/articles/s41587-019-0068-4

阅读级别：`abstract_plus_official_docs`。查阅位置：论文摘要；官方说明及 basic tutorial 页面。检索日：2026-09-24。

## 原文事实摘取（F）
将分化看作低维表型流形上的随机过程，以命运概率表征连续性和分支不确定性。

输入/输出：输入单细胞表征与起始状态等设定；输出伪时间、分支概率、分化潜能。

定位：Abstract；官方 Palantir / Basic Tutorial。

## 跨论文归纳的开发决策（S）
将“在轨迹上排序”与“对各终态的倾向”分成不同对象验证。

## 建议的新项目检查（P；本次未运行）
扰动起点、终态、流形和稀有分支；比较概率变化与排序变化。

## 解释边界与未决事项
分化潜能不是直接测量的生物学多能性。原论文全文访问受限；2019 年 author correction 的内容尚未核读。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
- https://palantir.readthedocs.io/en/latest/
- https://palantir.readthedocs.io/en/latest/notebooks/Palantir_sample_notebook.html

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
