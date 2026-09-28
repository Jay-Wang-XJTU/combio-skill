# P4 · ENVI / COVET

## 来源与范围
The covariance environment defines cellular niches for spatial inference  
Nature Biotechnology · 2024 在线；2025 卷期  
目标作者关联：Dana Pe'er（共同署名不等于个人独立贡献）。  
DOI：10.1038/s41587-024-02193-4  
原始来源：https://www.nature.com/articles/s41587-024-02193-4

阅读级别：`targeted_full_text`。查阅位置：Main；COVET 定义；ENVI 架构；插补评价及部分 Methods。检索日：2026-09-24。

## 原文事实摘取（F）
COVET 用相对总体均值的 shifted covariance 表征邻域；ENVI 同时学习表达与环境的解码。

输入/输出：输入空间表达及 scRNA 参考；输出共享 latent、空间未测基因的预测及单细胞环境预测。

定位：Fig. 1；Results COVET defines spatial neighborhoods / ENVI algorithm / gene holdout。

## 跨论文归纳的开发决策（S）
选表示时要明确保留组成、均值还是协变；预测空间环境与恢复唯一空间位置不是同一任务。

## 建议的新项目检查（P；本次未运行）
按基因及样本留出；保留测量/插补标记；检查参考缺失状态和邻域尺度。

## 解释边界与未决事项
COVET 不是局部均值中心化的普通 covariance；参考提供的未测基因信号仍是预测。

本卡不是全文摘要，也不代表补充材料与源代码已审计。模型数学、数据规模、参数和统计结论仅在本卡明确记录的范围内视为已核读；未填写项不视为不存在。

## 附加官方来源或代码入口
未另增官方材料。

代码状态：未逐行审计、未运行、未验证当前依赖。官方文档与论文版本可能不同，复现前须锁定论文对应版本。全文 PDF/SI 不打包；仅保留自己的概述和来源指针。

## v0.2复现状态补充
本篇原图/原数据在本轮未运行；完整SI未标记为已读。当前状态见[逐篇复现矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)。
