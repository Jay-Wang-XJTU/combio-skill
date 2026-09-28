# J1 · DeepST

## 来源与范围
DeepST: identifying spatial domains in spatial transcriptomics by deep learning  
Nucleic Acids Research · 2022  
目标作者关联：Qinghua Jiang（共同署名不等于个人独立贡献）。  
DOI：10.1093/nar/gkac901  
原始来源：https://academic.oup.com/nar/article/50/22/e131/6761985

阅读级别：`targeted_full_text`。查阅位置：Main；数据增强、图/自编码结构、domain adversarial 模块；benchmark Methods。检索日：2026-09-24。

## 原文事实摘取（F）
融合空间/组织信息和表达表征进行空间域识别；包括用于整合的领域对抗组件。

输入/输出：输入空间表达及可用的组织信息；输出表征、空间域与整合结果。

定位：Methods：data augmentation、DAN、benchmark K 设置。

## 跨论文归纳的开发决策（S）
融合收益需区分来自额外模态、预处理还是模型；公开是否用已知 domain 数量。

## 建议的新项目检查（P；本次未运行）
信息匹配消融；已知 K 与未知 K 分轨；域边界和非连续区域测试。

## 解释边界与未决事项
域识别效果不是通讯或动态证据；方法文中给定 K 的实验不代表真实任务已知 K。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
