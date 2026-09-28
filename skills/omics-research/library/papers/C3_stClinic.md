# C3 · stClinic

## 来源与范围
stClinic dissects clinically relevant niches by integrating spatial multi-slice multi-omics data in dynamic graphs  
Nature Communications · 2025  
目标作者关联：Luonan Chen（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41467-025-60575-x  
原始来源：https://www.nature.com/articles/s41467-025-60575-x

阅读级别：`targeted_full_text`。查阅位置：Main；Methods 图构建、GMM/VGAE、下游临床；Discussion 连续性限制。检索日：2026-09-24。

## 原文事实摘取（F）
图在训练中按聚类信息更新，整合空间及跨切片关系；作者同时指出删去跨簇边可能不利于连续结构。

输入/输出：输入多切片/模态表征与空间信息；输出 niche 表征及样本级临床分析。

定位：Discussion limitations；Methods dynamic graph、clinical analysis。

## 跨论文归纳的开发决策（S）
离散分区和连续状态建模有不同偏好；共同特征预处理的贡献必须单独记账。

## 建议的新项目检查（P；本次未运行）
审计删边前后桥接区域与连续梯度；患者级临床隔离；检查样本级聚合表示的稳定性。

## 解释边界与未决事项
dynamic graph 指算法训练中的图更新，不是直接重建生物时间。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。 本轮定向新增核查见[SI/源码审计](../audits/TARGETED_SOURCE_AUDIT.md)。
