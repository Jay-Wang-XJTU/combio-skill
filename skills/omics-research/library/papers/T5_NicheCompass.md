# T5 · NicheCompass

## 来源与范围
Quantitative characterization of cell niches in spatially resolved omics data  
Nature Genetics · 2025  
目标作者关联：Fabian Theis（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41588-025-02120-6  
原始来源：https://www.nature.com/articles/s41588-025-02120-6

阅读级别：`targeted_full_text`。查阅位置：Main、模型概述、Methods 起始部分、Discussion 的解释性限制、Code availability。检索日：2026-09-24。

## 原文事实摘取（F）
变分图模型结合程序先验及 masked 组学解码器；作者指出程序活性可能由靶基因或身份标记驱动，而非对应配体/TF。

输入/输出：输入空间组学、空间图和程序先验；输出 niche 表征及程序相关活性。

定位：模型概述；Discussion limitations；Authors/Contributions。

## 跨论文归纳的开发决策（S）
结构化先验是解释约束，不是解释真实性的最终证据；须验证分数究竟由哪些基因支撑。

## 建议的新项目检查（P；本次未运行）
拆分 ligand/TF、target、identity marker 的贡献；扰动先验；检查跨样本和跨 seed 的语义稳定性。

## 解释边界与未决事项
Theis 为共同作者，不能将该工作全部归为其主导；文中共同通讯作者为 C. Talavera-López 和 M. Lotfollahi。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
- https://github.com/Lotfollahi-lab/nichecompass
- https://github.com/Lotfollahi-lab/nichecompass-reproducibility

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。 本轮定向新增核查见[SI/源码审计](../audits/TARGETED_SOURCE_AUDIT.md)。
