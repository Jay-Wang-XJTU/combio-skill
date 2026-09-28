# T2 · scArches

## 来源与范围
Mapping single-cell data to reference atlases by transfer learning  
Nature Biotechnology · 2021 在线；2022 卷期  
目标作者关联：Fabian Theis（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41587-021-01001-7  
原始来源：https://www.nature.com/articles/s41587-021-01001-7

阅读级别：`targeted_full_text`。查阅位置：PMC 公开正文：摘要、Main、架构迁移及参考映射相关 Results。检索日：2026-09-24。

## 原文事实摘取（F）
通过 architecture surgery 将新数据映射到已有模型；条件变量扩展和有限参数更新支持参考模型的复用。

输入/输出：输入训练好的参考模型和 query；输出可比较表征及基于参考的分析结果。

定位：PMC 公开正文：摘要、Main、架构迁移及参考映射相关 Results。

## 跨论文归纳的开发决策（S）
参考构建、query 适配和独立预测是不同实验协议，必须分开声明。

## 建议的新项目检查（P；本次未运行）
按患者隔离；检查参考缺失状态、query 特有状态、适配前后参考漂移；对比不适配与允许适配。

## 解释边界与未决事项
不提供原始参考数据不等于经过证明的隐私保证；参考未覆盖的状态不能强制获得已知标签。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8763644/

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
