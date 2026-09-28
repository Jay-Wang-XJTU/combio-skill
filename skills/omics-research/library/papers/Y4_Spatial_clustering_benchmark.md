# Y4 · Spatial clustering benchmark

## 来源与范围
Benchmarking spatial clustering methods with spatially resolved transcriptomics data  
Nature Methods · 2024  
目标作者关联：Zhiyuan Yuan（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41592-024-02215-8  
原始来源：https://www.nature.com/articles/s41592-024-02215-8

阅读级别：`abstract_plus_extended_captions`。查阅位置：摘要；公开 Extended Data captions；完整 Methods/SI/peer review 未获取。检索日：2026-09-24。

## 原文事实摘取（F）
benchmark 区分空间 domain 和细胞类型，并考察连续性、非连续区域、规模与模拟扰动。

输入/输出：输入多平台真实/模拟 SRT 及相应参考；输出多维方法比较。

定位：Abstract；Extended Data captions；补充材料获取尝试失败。

## 跨论文归纳的开发决策（S）
先问标签对应什么生物学对象，再决定是否评价平滑或连续性。

## 建议的新项目检查（P；本次未运行）
分开连续组织层与非连续小病灶；标签不可信时不报告其为真值准确率。

## 解释边界与未决事项
本轮不能基于该文未读的 SI 复述全部参数、统计或宣称独立复现。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
