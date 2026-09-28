# C1 · CSN

## 来源与范围
Cell-specific network constructed by single-cell RNA sequencing data  
Nucleic Acids Research · 2019  
目标作者关联：Luonan Chen（共同署名不等于个人独立贡献）。  
DOI：10.1093/nar/gkz172  
原始来源：https://academic.oup.com/nar/article/47/11/e62/5377474

阅读级别：`targeted_full_text`。查阅位置：Main；局部统计依赖构网 Methods；network degree 表征及零值说明。检索日：2026-09-24。

## 原文事实摘取（F）
利用整个细胞群体中的局部统计依赖，为每个细胞构建基因关联网络，并以网络度形成另一种表征。

输入/输出：输入群体单细胞表达；输出 cell-specific 基因关联网络及 network degree matrix。

定位：Methods：局部依赖统计；Main：NDM；gene association 的解释边界。

## 跨论文归纳的开发决策（S）
新生物学信号可能位于关系变化而非表达均值变化；同时追踪估计依赖的参考群体。

## 建议的新项目检查（P；本次未运行）
重采样参考细胞；比较条件化前后网络；检测深度、零值、阈值和多重检验敏感性。

## 解释边界与未决事项
单细胞分辨率输出并非单个细胞独立估计；统计关联不能区分调控和其他相关来源。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
