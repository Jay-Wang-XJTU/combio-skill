# 五项缺口的v0.2状态与准入条件

日期2026-09-28。**“知识/技能已补入”不等于“全部论文复现已完成”。**本表按交付层次明确剩余工作。

|缺口|本版已加入并做了什么|仍未验证的部分|
|---|---|---|
|完整补充材料与代码复现|审计规范、44页NicheCompass SI的定向核读、stClinic正文/代码入口、POT/Meta路径源码核查、原图执行器、逐篇矩阵|全部20篇完整SI/全部源码/原图复现均未完成；官方软件没有运行|
|统计独立性与多重检验|donor层级、raw-count pseudobulk、配对/混杂/选择性检验、BH/BY、置换；反例模拟和数值检查|edgeR R模板未运行；真实NB数据、复杂层级/空间选择性推断、实际功效设计未验收|
|因果识别|DAG、backdoor、collider、中介、positivity、AIPW、crossfit、干扰/选择；合成已知ATE验证|未观测混杂无法由算法自动排除；真实干预、多donor cluster AIPW/干扰估计未实现验证|
|空间上游测量误差|分割/分子分配/ambient/spot bleed/坐标/参考误差；重建图和下游敏感性模拟|Baysor/Proseg/SpotClean/cell2location官方流程未运行；未用原始影像与分子数据校准误差|
|OT/FM专门理论实现|balanced/UOT目标与数值、KL参考、成本尺度、耦合/路径/ODE、质量语义；SciPy oracle和PyTorch CFM已运行|POT/Meta/CellFlow官方运行、非线性/多峰基准、大规模稀疏/GW、真实时序验证未完成|

## 不变的边界
20篇原文献阅读记录继承自v0.1，非本轮全部重新审读；来源索引35条记录明确标注摘要、正文、源码或作者入口，不能统称为35篇全文精读。38个agent行为案例未运行。结构/数值通过不能提升行为验证或临床校准状态。

## 后续准入不采用一个笼统的reproduced
- `supplement_full_read`：具体附件全部页面/图表核读，并列出其他未取得附件。
- `source_audited`：固定版本下的目标函数/关键数据流已核对。
- `upstream_executed`：实际官方软件命令、环境、日志和输出存在。
- `figure_reproduced`：原图对应数据/参数运行，预定定量验收通过。
- `behavior_tested`：另一个agent的真实回答和rubric记录存在。
- `biologically_validated`：匹配主张的独立生物学证据存在。

这些状态互不替代。下一次升级从[逐篇矩阵](audits/PAPER_REPRODUCTION_MATRIX.md)和[复现配置](workflows/reproduction_manifest.yaml)选定具体panel，不能批量翻转状态。

## 非本轮范围但仍重要
scATAC/多组学测量特性、完整生存/竞争风险与临床决策分析、全部软件版本跨平台可复现、真实项目与agent兼容性。它们不是被此次更新隐含解决。
