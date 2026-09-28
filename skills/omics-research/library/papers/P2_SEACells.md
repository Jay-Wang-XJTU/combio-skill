# P2 · SEACells

## 来源与范围
SEACells infers transcriptional and epigenomic cellular states from single-cell genomics data  
Nature Biotechnology · 2023  
目标作者关联：Dana Pe'er（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41587-023-01716-9  
原始来源：https://www.nature.com/articles/s41587-023-01716-9

阅读级别：`targeted_full_text`。查阅位置：Main；kernel/archetypal analysis Methods；metacell 纯度、紧凑性、分离度和比较设计。检索日：2026-09-24。

## 原文事实摘取（F）
使用核化 archetypal analysis 建立 metacells，以聚合稀疏测量而保留细胞状态。

输入/输出：输入单细胞 RNA 或 ATAC 等表征；输出软分配及聚合状态。

定位：Methods：adaptive kernel、archetypal analysis、comparison；统计依赖的作者说明。

## 跨论文归纳的开发决策（S）
分析单位本身是方法设计变量；降噪的收益应与稀有状态和连续变化的损失一起评价。

## 建议的新项目检查（P；本次未运行）
匹配聚合粒度再比较；测纯度、稀有状态保留和多模态一致性；统计重采样按来源样本组织。

## 解释边界与未决事项
聚合单元不自动成为独立生物学重复；不能把默认每个 metacell 的细胞数作为通用规则。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
