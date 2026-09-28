# v0.2阅读覆盖总入口

原20篇的阅读记录继承自v0.1，见下方历史表。本轮额外35条资料的准确范围见[GAP_SOURCES.md](GAP_SOURCES.md)和[gap_sources.json](gap_sources.json)；多条为同一论文的正文、代码或文档，不能合并声称为35篇全读论文。

本轮重点定向阅读：NicheCompass SI方法/评价、stClinic相关主文、POT unbalanced源码、Meta affine path源码、Chizat UOT算法与Tong CFM理论、Pearl识别、DML、Proseg和SpotClean正文相关部分。其余来源深度逐条列明。未取得全文的书稿/附件仍保留缺口。

[原论文运行矩阵](../audits/PAPER_REPRODUCTION_MATRIX.md)全部原图未运行；[实际六实验](../results/execution_report.json)属于独立合成/数值验证。这两类状态不可互换。

---

# 文献索引与阅读覆盖

检索与核读日期：2026-09-24。20 项研究按知识覆盖选择，不是引用量排名、穷尽书目或截至该日的最新工作清单。CellRank 2 同时属于两位目标作者，只计一次。

`targeted_full_text` = 定向阅读公开正文/相关方法段，不等于逐字通读全部正文和 SI。
`abstract_plus_official_docs` = 原论文访问有限，补读官方文档；不将当前文档自动视为原版实现。
`abstract_plus_extended_captions` = 仅摘要及公开扩展图注，未获取完整方法。

|ID|工作|目标作者|年份|阅读级别|证据卡|
|---|---|---|---|---|---|
|T1|scVelo|Fabian Theis|2020|abstract_plus_official_docs|[打开](../papers/T1_scVelo.md)|
|T2|scArches|Fabian Theis|2021 在线；2022 卷期|targeted_full_text|[打开](../papers/T2_scArches.md)|
|T3|CellRank 2|Fabian Theis, Dana Pe'er|2024|targeted_full_text|[打开](../papers/T3_CellRank_2.md)|
|T4|moscot|Fabian Theis|2025；DOI 含 2024|targeted_full_text|[打开](../papers/T4_moscot.md)|
|T5|NicheCompass|Fabian Theis|2025|targeted_full_text|[打开](../papers/T5_NicheCompass.md)|
|T6|scIB integration benchmark|Fabian Theis|2021 在线；2022 卷期|targeted_full_text|[打开](../papers/T6_scIB_integration_benchmark.md)|
|P1|Palantir|Dana Pe'er|2019|abstract_plus_official_docs|[打开](../papers/P1_Palantir.md)|
|P2|SEACells|Dana Pe'er|2023|targeted_full_text|[打开](../papers/P2_SEACells.md)|
|P3|Spectra|Dana Pe'er|2023 在线；2024 卷期|targeted_full_text|[打开](../papers/P3_Spectra.md)|
|P4|ENVI / COVET|Dana Pe'er|2024 在线；2025 卷期|targeted_full_text|[打开](../papers/P4_ENVI_COVET.md)|
|Y1|SOTIP|Zhiyuan Yuan|2022|targeted_full_text|[打开](../papers/Y1_SOTIP.md)|
|Y2|MENDER|Zhiyuan Yuan|2024|targeted_full_text|[打开](../papers/Y2_MENDER.md)|
|Y3|SPIRAL|Zhiyuan Yuan|2023|targeted_full_text|[打开](../papers/Y3_SPIRAL.md)|
|Y4|Spatial clustering benchmark|Zhiyuan Yuan|2024|abstract_plus_extended_captions|[打开](../papers/Y4_Spatial_clustering_benchmark.md)|
|C1|CSN|Luonan Chen|2019|targeted_full_text|[打开](../papers/C1_CSN.md)|
|C2|stKeep|Luonan Chen|2024|targeted_full_text|[打开](../papers/C2_stKeep.md)|
|C3|stClinic|Luonan Chen|2025|targeted_full_text|[打开](../papers/C3_stClinic.md)|
|J1|DeepST|Qinghua Jiang|2022|targeted_full_text|[打开](../papers/J1_DeepST.md)|
|J2|DeepCCI|Qinghua Jiang|2023|targeted_full_text|[打开](../papers/J2_DeepCCI.md)|
|J3|DeepTalk|Qinghua Jiang|2024|targeted_full_text|[打开](../papers/J3_DeepTalk.md)|

## 覆盖统计
17 项定向公开正文核读；2 项摘要加官方文档；1 项摘要加扩展图注。全部 20 项均未运行复现实验、未完成逐行代码审计、未完整阅读所有补充材料。

## 作者核验辅助来源
Zhiyuan Yuan 官方研究主页：https://istbi.fudan.edu.cn/lnen/info/1158/3301.htm
Luonan Chen 官方研究主页：https://soai.sjtu.edu.cn/cn/show/200
Qinghua Jiang 所在团队官方代码组织：https://github.com/JiangBioLab
具体归属以各论文的作者栏为准；参考文献或审稿人列表出现姓名不算共同作者。

## 补充材料访问失败
Y4 的 Supplementary Information 和公开 peer-review 文件获取失败。未读取其不可见内容，也没有据此宣称参数或复现结论。Palantir 的公开 PMC 全文在本轮访问中被验证页面阻挡。
