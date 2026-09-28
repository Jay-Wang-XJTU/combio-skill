# Codex 技能调用索引

本表为 0.2.1 的 29 个注册入口。共享库位于 `skills/omics-research/library/`。原工作流文件已改名 GUIDE.md；调用别名不变。

| 原编号 | Codex 调用 | 原技能标题 | 完整资料库路径 |
|---|---|---|---|
| 00 | `$omics-research` | 组学方法研究总路由 | `GUIDE.md` |
| 01 | `$omics-question` | 科学问题与可检验目标 | `skills/01-question-and-estimand/GUIDE.md` |
| 02 | `$omics-literature` | 研究缺口与先例核查 | `skills/02-literature-gap-and-prior-art/GUIDE.md` |
| 03 | `$omics-data` | 数据契约、覆盖与可行性 | `skills/03-data-contract-and-feasibility/GUIDE.md` |
| 04 | `$omics-representation` | 分析单位与多尺度表示 | `skills/04-analysis-unit-and-representation/GUIDE.md` |
| 05 | `$omics-preprocessing` | 观测模型与预处理兼容性 | `skills/05-observation-model-and-preprocessing/GUIDE.md` |
| 06 | `$omics-graph` | 图语义、采样和信息传播 | `skills/06-graph-and-message-passing-design/GUIDE.md` |
| 07 | `$omics-integration` | 整合、参考映射与配准分轨 | `skills/07-integration-and-reference-mapping/GUIDE.md` |
| 08 | `$omics-programs` | 可解释程序、语义对齐与证据 | `skills/08-interpretable-program-learning/GUIDE.md` |
| 09 | `$omics-dynamics` | 状态动态、命运与最优传输 | `skills/09-dynamics-fate-and-transport/GUIDE.md` |
| 10 | `$omics-mapping` | 空间映射、插补与误差传递 | `skills/10-spatial-mapping-and-imputation/GUIDE.md` |
| 11 | `$omics-communication` | 通讯、网络与标签来源审计 | `skills/11-communication-and-network-evidence/GUIDE.md` |
| 12 | `$omics-falsification` | 最小证伪实验与受控模拟 | `skills/12-minimum-falsification-and-simulation/GUIDE.md` |
| 13 | `$omics-benchmark` | 信息匹配与端到端 benchmark | `skills/13-information-matched-benchmarking/GUIDE.md` |
| 14 | `$omics-robustness` | 稳定性、可识别性与误差来源 | `skills/14-robustness-and-identifiability/GUIDE.md` |
| 15 | `$omics-clinical` | 统计单位与临床验证协议 | `skills/15-statistical-and-clinical-validation/GUIDE.md` |
| 16 | `$omics-biology` | 生物学发现与验证梯度 | `skills/16-biological-discovery-and-validation/GUIDE.md` |
| 17 | `$omics-engineering` | 可复现工程与规模边界 | `skills/17-engineering-and-scaling/GUIDE.md` |
| 18 | `$omics-evidence` | 主张—证据与论文组织 | `skills/18-claim-evidence-and-paper-design/GUIDE.md` |
| 19 | `$omics-code-audit` | 论文—代码—结果三方审计 | `skills/19-source-code-reproduction-audit/GUIDE.md` |
| 20 | `$omics-skill-maintenance` | Skill 验收与知识更新 | `skills/20-skill-evaluation-and-versioning/GUIDE.md` |
| 21 | `$omics-statistics` | 独立重复、分层切分与重采样 | `skills/21-independent-replicates-and-resampling/GUIDE.md` |
| 22 | `$omics-multiple-testing` | 多重检验与选择后推断 | `skills/22-multiple-testing-and-selective-inference/GUIDE.md` |
| 23 | `$omics-causal` | 因果识别、干预与机制证据 | `skills/23-causal-identification-and-perturbations/GUIDE.md` |
| 24 | `$omics-spatial-qc` | 空间测量链与上游误差审计 | `skills/24-spatial-upstream-measurement-error/GUIDE.md` |
| 25 | `$omics-ot` | OT/UOT理论、数值与质量语义 | `skills/25-optimal-transport-theory-and-numerics/GUIDE.md` |
| 26 | `$omics-flow-matching` | Flow matching配对、路径与ODE验证 | `skills/26-flow-matching-design-and-validation/GUIDE.md` |
| 27 | `$omics-reproduction` | 补充材料到源码与原图复现 | `skills/27-supplement-to-code-reproduction/GUIDE.md` |
| 28 | `$omics-uncertainty` | 分层不确定性、传播与校准 | `skills/28-uncertainty-propagation-and-calibration/GUIDE.md` |

## 类别分组

| 类别 | 原编号 |
|---|---|
| 定题与数据 | 01、02、03 |
| 模型与最小实验 | 04、05、06、12 |
| 空间整合与通讯 | 07、10、11、24 |
| 程序解释与稳健性 | 08、14 |
| 动态与 OT/FM | 09、25、26 |
| 统计与不确定性 | 15、21、22、28 |
| 因果与生物学发现 | 16、23 |
| Benchmark、工程与复现 | 13、17、19、27 |
| 论文与技能维护 | 18、20 |

分类用于选工作流，不是宿主中的文件夹类别或独立 agent。安装 profile 与这些概念分组可以有交叉。
