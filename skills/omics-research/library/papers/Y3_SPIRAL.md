# Y3 · SPIRAL

## 来源与范围
SPIRAL: integrating and aligning spatially resolved transcriptomics data across different experiments, conditions, and technologies  
Genome Biology · 2023  
目标作者关联：Zhiyuan Yuan（共同署名不等于个人独立贡献）。  
DOI：10.1186/s13059-023-03078-6  
原始来源：https://link.springer.com/article/10.1186/s13059-023-03078-6

阅读级别：`targeted_full_text`。查阅位置：Main；两模块架构；空间图、domain adaptation、cluster-aware GW 和模拟。检索日：2026-09-24。

## 原文事实摘取（F）
分开进行表示整合与空间对齐；整合用图和领域适配，对齐使用 cluster-aware GW。

输入/输出：输入多切片表达与坐标；输出整合表示，以及条件适当时的空间对齐。

定位：Main/Results：SPIRAL integration and alignment；simulation。

## 跨论文归纳的开发决策（S）
表达状态可比与组织坐标对应应有独立任务定义和验收。

## 建议的新项目检查（P；本次未运行）
测试共有/特异区域；比较只整合与再配准；评估批次去除与局部组织保留。

## 解释边界与未决事项
不同患者肿瘤未必存在可配准的同源结构；不能仅因能计算变换就声称解剖对应。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
