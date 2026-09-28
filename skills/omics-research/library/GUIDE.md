---
name: omics-method-research-router
description: 为单细胞和空间组学方法课题选择问题定义、数据、统计、因果、空间误差、OT/FM、审计与验证技能。
version: 0.2.0
status: literature-derived-with-scoped-numerical-checks
---

# 研究开发路由

先读README、AGENTS和coverage_gaps，只载入当前决策需要的技能。为每项结论标注F/S/P/E与证据范围。不能用新模型替代不可识别性分析，不能用toy tests代替原论文复现。

## 条件分支
|遇到的问题|先调用|必须得到的结果|
|---|---|---|
|定题、找数据、界定创新|01–03|目标量、最近先例、数据可行性与独立单位|
|表示、模型、图设计|04–06、12|输入语义、强简单基线、可证伪的最小实验|
|整合、程序、动态、映射、通讯|07–11|对应任务契约及解释边界|
|样本差异、患者泛化、置信区间|15、21、28|重复单位/切分/检验/重采样分别定义|
|很多基因、程序、尺度、命运的显著性|22|预定检验家族、有效p值、selection处理|
|driver、干预、反事实或机制|16、23|DAG、识别条件、混杂/中介/选择/干扰|
|分割、坐标、混合、反卷积影响下游|05、10、24、28|上游误差来源、传播链、敏感性或校准标签|
|OT对应或UOT质量变化|09、25|成本/质量/参考测度合同及求解器残差|
|Flow matching / 神经ODE|09、25、26|耦合、路径、速度目标、积分器与实际边际|
|benchmark与稳健性|13–16、21–24|信息匹配、公平指标、独立生物学证据|
|复现、部署、出论文|17–19、27|版本、输入、命令、日志、定量验收与主张证据|
|更新技能库|20、28|来源/代码/数值/agent行为各自的验证状态|

## 输出约束
每次任务结束应给出：当前能作出的判断、证据来源、尚未成立的结论、下一项最有区分力的实验。需要输入时先读已有项目文件；不存在的信息保留为空并说明，不猜患者数、版本、阈值或运行结果。

## 技能入口
- [01-question-and-estimand · 科学问题与可检验目标](skills/01-question-and-estimand/GUIDE.md)：提出新计算方法、项目启动或模型目标反复改变时。
- [02-literature-gap-and-prior-art · 研究缺口与先例核查](skills/02-literature-gap-and-prior-art/GUIDE.md)：声称创新、选 baseline 或命名新任务前。
- [03-data-contract-and-feasibility · 数据契约、覆盖与可行性](skills/03-data-contract-and-feasibility/GUIDE.md)：找数据、下载、合并批次或设计 train/test 前。
- [04-analysis-unit-and-representation · 分析单位与多尺度表示](skills/04-analysis-unit-and-representation/GUIDE.md)：选择 cell/metacell/niche 表示，或要证明超越细胞组成时。
- [05-observation-model-and-preprocessing · 观测模型与预处理兼容性](skills/05-observation-model-and-preprocessing/GUIDE.md)：选 NB/Poisson/MSE、组合模态、训练生成模型或移植基线时。
- [06-graph-and-message-passing-design · 图语义、采样和信息传播](skills/06-graph-and-message-passing-design/GUIDE.md)：构造 GNN、跨切片图、异构图或子图编码器时。
- [07-integration-and-reference-mapping · 整合、参考映射与配准分轨](skills/07-integration-and-reference-mapping/GUIDE.md)：跨样本、患者、平台整合或将新样本映射到 atlas 时。
- [08-interpretable-program-learning · 可解释程序、语义对齐与证据](skills/08-interpretable-program-learning/GUIDE.md)：基因程序 latent、masked decoder、gene-set priors 或 driver 排名时。
- [09-dynamics-fate-and-transport · 状态动态、命运与最优传输](skills/09-dynamics-fate-and-transport/GUIDE.md)：伪时间、命运推断、跨时间 OT 或连续状态建模时。
- [10-spatial-mapping-and-imputation · 空间映射、插补与误差传递](skills/10-spatial-mapping-and-imputation/GUIDE.md)：用 scRNA 补空间基因、spot 反卷积、推断单细胞空间上下文时。
- [11-communication-and-network-evidence · 通讯、网络与标签来源审计](skills/11-communication-and-network-evidence/GUIDE.md)：LR 互作、基因网络、链接预测或通讯解释时。
- [12-minimum-falsification-and-simulation · 最小证伪实验与受控模拟](skills/12-minimum-falsification-and-simulation/GUIDE.md)：大规模训练前，或要判断新增模块是否必要时。
- [13-information-matched-benchmarking · 信息匹配与端到端 benchmark](skills/13-information-matched-benchmarking/GUIDE.md)：比较方法、组织 benchmark 或声明性能优越时。
- [14-robustness-and-identifiability · 稳定性、可识别性与误差来源](skills/14-robustness-and-identifiability/GUIDE.md)：多 seed 不一致、解释易变或准备报告稳健性时。
- [15-statistical-and-clinical-validation · 统计单位与临床验证协议](skills/15-statistical-and-clinical-validation/GUIDE.md)：患者分期、生存、治疗响应或样本差异分析时。
- [16-biological-discovery-and-validation · 生物学发现与验证梯度](skills/16-biological-discovery-and-validation/GUIDE.md)：从计算结果提出 marker、program、driver、niche 机制时。
- [17-engineering-and-scaling · 可复现工程与规模边界](skills/17-engineering-and-scaling/GUIDE.md)：实现新方法、HPC 批量实验或声称可扩展时。
- [18-claim-evidence-and-paper-design · 主张—证据与论文组织](skills/18-claim-evidence-and-paper-design/GUIDE.md)：组织 Results、选主图、写摘要或回应审稿时。
- [19-source-code-reproduction-audit · 论文—代码—结果三方审计](skills/19-source-code-reproduction-audit/GUIDE.md)：移植模型、复现 baseline、确认论文实现或发布 skill 前。
- [20-skill-evaluation-and-versioning · Skill 验收与知识更新](skills/20-skill-evaluation-and-versioning/GUIDE.md)：把文献归纳成 skill、更新规则或交给 agent 长期调用时。
- [21-independent-replicates-and-resampling · 独立重复、分层切分与重采样](skills/21-independent-replicates-and-resampling/GUIDE.md)：设计患者泛化、单细胞/空间差异检验、模型性能误差条或bootstrap时。
- [22-multiple-testing-and-selective-inference · 多重检验与选择后推断](skills/22-multiple-testing-and-selective-inference/GUIDE.md)：报告显著gene/program/LR/niche、挑选driver、先聚类/拟合pseudotime再检验时。
- [23-causal-identification-and-perturbations · 因果识别、干预与机制证据](skills/23-causal-identification-and-perturbations/GUIDE.md)：声称driver、调控因果、反事实、干预效果或“恶变概率”时。
- [24-spatial-upstream-measurement-error · 空间测量链与上游误差审计](skills/24-spatial-upstream-measurement-error/GUIDE.md)：构造空间图、发现罕见混合状态/界面生态位、比较分割或推断通讯前。
- [25-optimal-transport-theory-and-numerics · OT/UOT理论、数值与质量语义](skills/25-optimal-transport-theory-and-numerics/GUIDE.md)：用OT做时间对应、整合、空间匹配或作为FM配对时。
- [26-flow-matching-design-and-validation · Flow matching配对、路径与ODE验证](skills/26-flow-matching-design-and-validation/GUIDE.md)：从状态分布学习向量场、连接UOT与FM、解释轨迹/箭头/命运时。
- [27-supplement-to-code-reproduction · 补充材料到源码与原图复现](skills/27-supplement-to-code-reproduction/GUIDE.md)：把文献经验升级为具体实现、迁移算法或声称“已复现”时。
- [28-uncertainty-propagation-and-calibration · 分层不确定性、传播与校准](skills/28-uncertainty-propagation-and-calibration/GUIDE.md)：整合多个模型/测量阶段、汇报置信区间、稳健性或恶变风险分数时。
