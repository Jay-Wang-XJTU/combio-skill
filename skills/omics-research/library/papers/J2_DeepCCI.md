# J2 · DeepCCI

## 来源与范围
DeepCCI: a deep learning framework for identifying cell–cell interactions from single-cell RNA sequencing data  
Bioinformatics · 2023  
目标作者关联：Qinghua Jiang（共同署名不等于个人独立贡献）。  
DOI：10.1093/bioinformatics/btad596  
原始来源：https://academic.oup.com/bioinformatics/article/39/10/btad596/7281356

阅读级别：`targeted_full_text`。查阅位置：Main/Methods：聚类与 CCI 双模型、LRIDB、多亚基、数据处理及训练标签生成。检索日：2026-09-24。

## 原文事实摘取（F）
AE/GCN 用于聚类，监督 GCN 用于 CCI；训练标签来自其他统计方法的显著结果与相应打分规则。

输入/输出：输入 scRNA、互作先验及构造的监督标签；输出细胞簇与候选簇间互作。

定位：Methods：2.1、2.2、模型部分及 CCI label construction。

## 跨论文归纳的开发决策（S）
标签的来源决定模型实际学习的任务；必须区分工具共识、文献先验和独立实验真值。

## 建议的新项目检查（P；本次未运行）
先做简单 LR 分数/标签生成器基线；审计未标注负例；按样本、互作或数据库来源设置留出。

## 解释边界与未决事项
与标签来源工具一致不是独立的真实通讯证明；不应把所有未检出互作认定为真阴性。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
