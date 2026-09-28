# 从代表性方法论文提取的研究开发知识

## 0. 这份知识底座回答什么

目标不是复刻五个团队的模型菜单，而是形成能够回答以下问题的操作知识：**面对一项生物学需求和一组不完美数据，怎样定义任务、设计最小方法、建立可信证据，并知道何时应该调整或收缩结论。**

阅读截至 2026-09-24，选取 20 项研究。17 项定向读取了可获得的正文/方法相关段落；scVelo 与 Palantir 为论文摘要加官方文档；空间 clustering benchmark 为摘要加公开扩展图注。没有完整通读所有 SI，没有审计全部代码，没有运行复现。见 [逐项阅读覆盖](references/READING_COVERAGE.md)。

本报告的操作要求属于 **S（综合规则）或 P（拟验证建议）**；论文事实 F 集中在 `papers/` 的简短证据卡中。文献 ID 可在下方索引定位。不能据此声称每项检查都在原论文中完成过。

## 1. 五组论文分别贡献了什么知识

|共同署名作者|本轮选取|在知识底座中的主要作用|
|---|---|---|
|Fabian Theis|T1 scVelo；T2 scArches；T3 CellRank 2；T4 moscot；T5 NicheCompass；T6 scIB benchmark|观测与方向假设、模块化命运推断、参考迁移、传输对应、程序约束、多目标验证|
|Dana Pe’er|P1 Palantir；P2 SEACells；P3 Spectra；P4 ENVI/COVET；另有共享 T3|连续状态、不确定性、分析单位、功能程序与身份分离、环境表示|
|Zhiyuan Yuan|Y1 SOTIP；Y2 MENDER；Y3 SPIRAL；Y4 空间 clustering benchmark|对象与距离设计、多尺度组成、整合/配准分离、任务匹配的空间评价|
|Luonan Chen|C1 CSN；C2 stKeep；C3 stClinic|关系层信号、异构知识图、多切片图学习、临床聚合及连续性边界|
|Qinghua Jiang|J1 DeepST；J2 DeepCCI；J3 DeepTalk|模态融合、监督标签来源、子图上下文、映射—通讯的多级验证|

这是本轮选文形成的能力分工，不是对作者整体研究范围或能力的评级。特别是 T5 中 Theis 为共同作者，不将该工作写成其个人主导。

## 2. 首先掌握：任务和目标量的语言

方法开发要从一张问题卡开始，而不是从模型图开始：

> 生物学问题 → 决策用途 → 分析单位 → 观测数据 → 目标量 → 假设 → 可推翻结论的实验。

例如“识别早期恶变风险 niche”，至少可能代表四种任务：描述早期样本中的异常局部状态；区分已知 early/advanced 样本；估计跨阶段状态对应；预测当前早期患者未来发生恶变。它们不是同一主张，最后一种尤其需要相应随访、结局和独立验证设计。只有横截面数据时，可以研究候选风险相关状态，但不能把阶段分类分数直接更名为已校准的未来风险。

应区分三种尺度：**观测尺度、表征尺度、推断/统计尺度**。细胞是观测对象，niche 可以是表示对象，而泛化到患者的推断需要患者层面的验证。metacell 或重叠子图增加分析单元数量，不等于新增独立患者。

P2、P4、Y1、Y2 提示应把“如何定义研究对象”纳入创新空间，而非假定每个细胞只有一种天然表示。对应技能：01、03、04。

## 3. 数据契约：模型使用了什么信息

必须记录层级 ID、物种、技术平台、panel、计数定义、空间坐标单位、组织区域、患者阶段、治疗、随访、测量和推断的区别。具体项目允许字段变化，但不能只有一个无语义的矩阵文件。

对空间任务，至少审计：spot 是否混合多细胞；FOV 边界；分割/检测偏差；不均匀密度；各切片 panel 与尺度差异；病理注释的粒度和获取方式。对时间任务，还要记录真实采样时间、是否纵向配对、是否有 velocity/谱系、各时间采样比例。对 multi-omics，要区分同细胞配对、同样本不同细胞和完全不配对。

每条数据处理链保留：原始测量 → QC → feature selection → 标准化/观测目标 → 表示学习 → 下游模型 → 评价。独立预测任务的数据隔离必须覆盖整条链；联合分析场景允许使用待整合数据，但要明确其不是未见样本部署测试。

**最关键的设计检查是可分辨性。** 当阶段与平台完全一致时，算法不能单凭该设计被证明去除了平台而保留阶段。应补交叉设计、外部数据或收缩结论，而不是把混合图当作分离成功。对应 T2、T6、P4、J3；技能 03、07、15。

## 4. 表示学习不是单选题：信息保留清单

为候选表示建立一张“保留/忽略/需验证”表：

|候选表示|直接编码的内容|需要专门检查的代价|
|---|---|---|
|中心表达|中心细胞状态|忽略环境，可能不足以唯一预测 niche|
|单尺度组成|邻居状态比例或数量|离散标签分辨率、状态内部变化|
|多尺度组成|不同距离范围内的组成|物理尺度与密度依赖|
|邻域均值|总体表达平均|不同混合模式可能有相同均值|
|协变表征|邻域基因/状态协变|估计样本量、参考均值、特征维数成本|
|子图/异构图|指定边和属性所携带的局部关系|边来源、采样、重复节点、过度传播|
|程序约束 latent|先验引导的功能表征|先验不完整、冗余及语义可识别性|

这张表是候选设计空间，不是性能排名。选择要由研究目标和最小实验决定。SOTIP、MENDER、COVET 与 NicheCompass 提供不同的对象和建模选择，不能把它们都简化成“另一个 GNN”。详见 Y1、Y2、P4、T5。

适合的最小测试是：固定组成改变几何；固定几何改变状态；固定均值改变协变；固定生物学改变深度/平台。**实际希望区分的改变应该产生信号；应忽略的改变不应成为主导因素。** 这是我们提出的设计验收，不是声称每篇论文都做了该完整实验矩阵。

## 5. 数学与实现必须理解到什么粒度

不要求所有任务使用以下全部方法，但被选中的组件必须理解到能检查其假设和实现。

|知识块|至少能够回答|相应文献入口|
|---|---|---|
|观测 likelihood|输入/重建目标的支持集是什么？计数、log 值、比例能否用同一分布？|T1、T5、P4|
|变分学习|编码的是后验参数还是确定性向量？KL、重建和协变量各约束什么？|T2、T5、P4、C3|
|矩阵分解与先验|哪些自由度被 mask/penalty 固定？哪些排列、缩放或冗余仍存在？|P3、T5|
|图传播|邻接归一化、自环、边方向、attention 的条件集合与采样如何影响表示？|C2、C3、J1、J3|
|连续流形/Markov 模型|方向来自哪里？哪些状态可达？终态改变时概率如何变？|P1、T3|
|RNA 动力学|哪些测量支撑反应拟合？相图和残差是否支持给出的方向？|T1|
|最优传输|运输什么对象、用什么代价、是否匹配质量、结构项如何改变意义？|T4、Y1、Y3、P4|
|统计依赖网络|边依据哪个群体的联合/边际统计？混杂与零值如何影响边？|C1|
|多目标优化|每个 loss 鼓励保留什么、去掉什么？损失之间是否冲突？|T5、T6、C3|
|近似与规模|稀疏、低秩、采样、近似距离的误差怎样传到生物学结论？|T4、P4、Y2|

例如，一个一般性的吸收 Markov 模型可把转移矩阵拆成瞬态之间的 Q 和瞬态到吸收态的 R。若所有相关瞬态最终可吸收，则命运矩阵 F 满足 `(I-Q)F=R`。这提供数值检查，但不证明 Q、终态选择或生物学方向正确。该公式是基础模型说明，不是把某一论文的全部求解过程重写成这一个等式。

又如，一个示意性的 masked 线性 decoder `X_hat = g(Z (W ⊙ M)^T + b)` 中，M 的零限制直接连接，但不能单凭该约束证明 Z 的每一维是唯一可识别的生物学机制。非线性链接 g、程序重叠、训练目标和其他通路仍需分析。

本轮没有完成这些领域的全套理论证明、原始基础论文或所有代码审计。以上是技能所需的理论能力清单，不能用“读过应用论文”替代。特别是 flow matching、因果识别和完整生存统计理论须另建专题。

## 6. 模型设计采用“问题—机制—实验”账本

每个模块都要回答：它弥补哪个明确困难？输入哪些额外信息？预期改变什么？删去或替换后能否证伪其必要性？有无更简单替代？

例如：空间图用于传播局部信息；跨样本匹配边用于联系表征；程序先验用于限制解释空间；去批次损失用于抑制技术差异。它们可能彼此冲突：对齐过强会抹去疾病状态，聚类分离过强会切断连续桥，程序约束过强会把数据压回先验。

因此需要 loss ledger：每个目标、作用层、系数、梯度流、数据来源、预期保留/去除的信息和对应测试。不能只比较一个加权总 loss。C3 的连续性限制是应当主动寻找这类冲突的具体入口；C2/J1 的额外信息说明融合模型还需要信息预算。技能 05、06、12。

## 7. 整合、参考映射、物理配准与时间对应必须分开

联合整合解决多个已见数据集的表示兼容；参考映射解决对已建参考的复用与适配；物理配准需要有意义的解剖对应；时间对应需要方向和采样假设。T2、Y3、T4 提供不同场景，不宜统称“跨切片 alignment”。

应设两个清单：需要忽略的变量，以及必须保留的变量。然后分别验证共有细胞状态、样本特有状态、连续生物学轴和稀有群体。细胞类型分得开不代表类型内部功能变化被保留，batch 混得均匀也不保证没有过整合。T6 是这类多目标框架的入口。

参考迁移还需一个拒绝或低置信分支：参考没有某状态时，方法应被允许表明缺少支持，而不是默认分给最近已知类型。模型适配是否使用 query、标签是否参与、适配是否改变参考，要在报告中明确。技能 07、13。

## 8. 动态模型：先检查方向，再谈轨迹

由状态距离可以定义相似关系，但时间方向需要额外依据。伪时间起点、RNA 动力学、真实时间点、代谢标记和谱系信息代表不同证据与假设。T1、P1、T3 说明动态推断并非单一模型路线。

最优传输还需回答被匹配的究竟是什么：Y1 的微环境分布距离不是细胞迁移；Y3 的结构对齐不是时间祖先；T4 的时间对应也仍依赖代价和质量等假设。**算法名字相同，不代表目标量相同。**

仅有不配对的 early/late 观测时，应将模型输出写成条件于假设的对应或候选连续过程。要检查不同合理代价、质量、采样、root 和 terminal 的敏感性，并尽可能用独立中间时间或谱系测试。把某条平滑插值画出来不是其真实发生的证据。

此外，算法训练时更新的 dynamic graph 与生物学动态不同。C3 的图更新可以用于整合和分区，但不能仅因名字包含 dynamic 就归为时间过程重建。技能 09。

## 9. 可解释性必须拆成可检查的层次

首先确定解释对象：latent 轴、program 活性、基因贡献、互作边、命运倾向还是机制。然后分别评价：

- **结构约束：**模型允许哪些依赖，不允许哪些依赖？
- **数据支持：**该分数由什么测量与基因支撑，能否解释相关变化？
- **语义稳定：**跨训练、样本与状态是否仍指向同一概念？
- **外部证据：**独立刺激、蛋白、谱系或干预是否支持该解释？

T5 和 P3 是两种不同的程序约束入口，不能混写成同一个 masked VAE。程序与输入 gene set 的相似性只回答部分先验一致性；同一先验不能再被重复作为完全独立的验证。

稳定性也分对象：重建稳定、命运预测稳定、program 排名稳定、top drivers 稳定。出现“预测尚可但解释不稳定”时，应降低解释层面的主张，而不是未经分析就宣布所有输出无效。反之也不能用预测稳定为不稳定的 driver 背书。技能 08、14、16。

## 10. 网络与通讯：最需要明确标签从哪里来

C1 的网络边是统计依赖，J2/J3 的互作推断涉及先验和学习目标，C2/T5 则在关系或程序表征中融入生物知识。应分别审计：数据库允许的候选、表达支持、空间接近、模型给出的链接和功能证据。

如果监督标签来自其他工具的显著结果，模型首先学的是该标注规则。能较好预测这种标签可以是有价值的工程结果，但不等于有独立实验真值。J2 是标签来源审计的具体案例。未被工具检出的边也不应不加区分地解释为真实阴性。

需要建立 label provenance ledger：标签生成方法、阈值、数据库、正负例、是否使用测试信息、独立性与验证来源。对多亚基复合物、分泌/接触范围和检测率，设定与任务相符的生物学可行性检查。

多阶段系统还需独立验证每一步：J3 中映射/插补与通讯是不同任务。上游基因插补或定位变好不能替代下游互作验证；推断坐标和真实测量坐标必须分开保存。技能 10、11。

## 11. Benchmark 至少有两条比较轨道

**信息匹配轨道：**限制可用信息一致，在相近的输入语义和下游评价条件下比较表征或算法能力。

**端到端轨道：**各方法采用合理的完整推荐流程，评价实际使用价值，同时公开额外信息、预处理、模型适配和计算成本。

两条轨道都合理，但不能把第二条的收益全部归因于模型架构。额外病理标签、图像、已知 K、外部预训练、先验数据库和更强的前处理必须记账。C2、J1、C3 是值得检查这些条件的入口。

评价至少需要任务匹配、对照充分、单位正确和失败透明。空间 domain 与细胞类型并非同一对象；非连续小病灶不能被一个偏好处处平滑的指标天然判差。无可信 domain 标签时应采用其他适当任务，不创造伪真值。对应 T6、Y4。

报告效应量和样本层级不确定性，并关注效能/生物学保留/成本的取舍。不能拿某篇 benchmark 采用的总分权重作为所有任务的合格线。技能 13。

## 12. 从探索性结果到可支持的生物学结论

每个候选发现配一张解释卡：新在哪里、输入先验是否已经包含、竞争解释是什么、哪项证据排除了哪项竞争解释、还缺什么。恢复一个已知 marker 可以是 sanity check，但不自动是新机制。

验证应与主张相称。一个算法可用性的主张可能主要需要模拟、独立数据和可复现比较；一个“某因子驱动命运”的主张则需要更强的鉴别性证据。T4 的新数据及敲除验证、P3 的已知刺激验证提供设计入口，而不是要求每个项目机械复制相同实验。

临床结果还要区分横截面关联、分类能力、未来风险与因果机制。患者级独立性、随访起点、删失、事件量、校准和混杂是需要专门学习与审计的内容；本轮应用论文不足以替代完整的临床统计培训。技能 15、16。

## 13. 从零启动的实际推进关卡

|关卡|应形成的产物|何时不应继续堆模型|
|---|---|---|
|G0 问题成立|问题卡、先例矩阵、主要主张|没有可验证缺口，或简单方法已足够|
|G1 数据可支撑|数据契约、混杂与标签审计|关键目标与可得数据不匹配|
|G2 核心机制可工作|简单基线、最小反例、数值检查|在最有利小场景仍无目标能力|
|G3 比较可信|两轨 benchmark、资源与失败表|优势只来自额外信息或评价偏差|
|G4 解释与迁移有边界|稳定性、独立样本、解释证据|关键结论依赖任意设定或循环验证|
|G5 结论可复核|主张证据表、配置、数据/代码版本|图无法追溯或复现与文字不一致|

关卡不是不可逆瀑布流程。验证发现新混杂时可以回到 G1；缺口不成立时可以改变研究目标。阈值应按具体主张、噪声和实际用途预先设定，不存在本包统一规定的“合格分数”。

## 14. 工程层也是科学证据的一部分

必须能追踪从数据版本、预处理、图、先验、seed、训练配置到每张图的来源。保存错误和失败状态；近似求解、采样和缓存要验证是否改变关键结论。算法规模不能只看网络参数，所有样本对距离、基因对协方差、重复子图和全局耦合都可能是瓶颈。

论文—代码核对至少覆盖目标函数、mask、采样、参数共享、梯度流、数据变换、训练与推断路径。可运行不等于数值复现，数值近似不等于全部生物学结论得到复现。本轮尚未进行此审计，应保持准确状态。技能 17、19。

## 15. 对 DyMoTree 与 NicheFlux 的应用示例（建议，不是已验证结论）

**DyMoTree：**分别定义表达重建、命运输出、program 语义和 driver 选择的验收。共享 decoder 可以提供共同参数化，但必须继续审计程序重叠、尺度和语义稳定。不能以命运分数稳定替代 program 排名稳定，也不能仅凭某个重建相关性否定所有用途。

**NicheFlux：**先验证 niche 表示是否比组成/多尺度基线保留更多与目标有关的信息，再测试跨样本整合是否保留早晚期状态，最后才把表示用于动态候选对应。跨患者切片不默认可物理配准；局部邻域重叠不增加患者数；OT 或后续生成路径不自动证明真实恶变过程。

这些示例只是将通用规则映射到项目语境，不构成模型改动、重训练或已完成的实验。该 skill 集合应能服务其他单细胞和空间计算方法，不固化为这两个项目专用流程。

## 16. 尚未掌握/验证到可以固化的内容

“所有需要理解的知识”不能通过有限代表作一次封闭。当前已建立的是核心问题清单、方法选择逻辑和证据审计路线。继续发布更可靠的 skill 还需要：完整 SI/代码对照与复现；统计独立性与多重检验的专门文献；因果识别与干预建模；分割/反卷积误差；OT/flow matching 的理论和实现；真实 agent 工作流验收。

未取得的材料、未运行的实验和矛盾结论在 [coverage_gaps.md](coverage_gaps.md) 中显式记录。**不把缺失证据写成既有知识，是这个知识底座最重要的规则之一。**

## 17. 来源索引

本文的 T/P/Y/C/J 编号对应 [20 项文献索引](references/READING_COVERAGE.md) 和 `papers/` 中证据卡。每张卡给出原文题目、DOI、原始链接、核读位置及阅读局限。需要复述具体数字、参数、实验条件或正式引用时，应回到相应原文并核查版本，不以本报告代替原论文。

### 完整原始文献入口

**T1 · scVelo** — Generalizing RNA velocity to transient cell states through dynamical modeling. Nature Biotechnology, 2020. DOI: 10.1038/s41587-020-0591-3. https://www.nature.com/articles/s41587-020-0591-3

**T2 · scArches** — Mapping single-cell data to reference atlases by transfer learning. Nature Biotechnology, 2021 在线；2022 卷期. DOI: 10.1038/s41587-021-01001-7. https://www.nature.com/articles/s41587-021-01001-7

**T3 · CellRank 2** — CellRank 2: unified fate mapping in multiview single-cell data. Nature Methods, 2024. DOI: 10.1038/s41592-024-02303-9. https://www.nature.com/articles/s41592-024-02303-9

**T4 · moscot** — Mapping cells through time and space with moscot. Nature, 2025；DOI 含 2024. DOI: 10.1038/s41586-024-08453-2. https://www.nature.com/articles/s41586-024-08453-2

**T5 · NicheCompass** — Quantitative characterization of cell niches in spatially resolved omics data. Nature Genetics, 2025. DOI: 10.1038/s41588-025-02120-6. https://www.nature.com/articles/s41588-025-02120-6

**T6 · scIB integration benchmark** — Benchmarking atlas-level data integration in single-cell genomics. Nature Methods, 2021 在线；2022 卷期. DOI: 10.1038/s41592-021-01336-8. https://www.nature.com/articles/s41592-021-01336-8

**P1 · Palantir** — Characterization of cell fate probabilities in single-cell data with Palantir. Nature Biotechnology, 2019. DOI: 10.1038/s41587-019-0068-4. https://www.nature.com/articles/s41587-019-0068-4

**P2 · SEACells** — SEACells infers transcriptional and epigenomic cellular states from single-cell genomics data. Nature Biotechnology, 2023. DOI: 10.1038/s41587-023-01716-9. https://www.nature.com/articles/s41587-023-01716-9

**P3 · Spectra** — Supervised discovery of interpretable gene programs from single-cell data. Nature Biotechnology, 2023 在线；2024 卷期. DOI: 10.1038/s41587-023-01940-3. https://www.nature.com/articles/s41587-023-01940-3

**P4 · ENVI / COVET** — The covariance environment defines cellular niches for spatial inference. Nature Biotechnology, 2024 在线；2025 卷期. DOI: 10.1038/s41587-024-02193-4. https://www.nature.com/articles/s41587-024-02193-4

**Y1 · SOTIP** — SOTIP is a versatile method for microenvironment modeling with spatial omics data. Nature Communications, 2022. DOI: 10.1038/s41467-022-34867-5. https://www.nature.com/articles/s41467-022-34867-5

**Y2 · MENDER** — MENDER: fast and scalable tissue structure identification in spatial omics data. Nature Communications, 2024. DOI: 10.1038/s41467-023-44367-9. https://www.nature.com/articles/s41467-023-44367-9

**Y3 · SPIRAL** — SPIRAL: integrating and aligning spatially resolved transcriptomics data across different experiments, conditions, and technologies. Genome Biology, 2023. DOI: 10.1186/s13059-023-03078-6. https://link.springer.com/article/10.1186/s13059-023-03078-6

**Y4 · Spatial clustering benchmark** — Benchmarking spatial clustering methods with spatially resolved transcriptomics data. Nature Methods, 2024. DOI: 10.1038/s41592-024-02215-8. https://www.nature.com/articles/s41592-024-02215-8

**C1 · CSN** — Cell-specific network constructed by single-cell RNA sequencing data. Nucleic Acids Research, 2019. DOI: 10.1093/nar/gkz172. https://academic.oup.com/nar/article/47/11/e62/5377474

**C2 · stKeep** — Dissecting tumor microenvironment from spatially resolved transcriptomics data by heterogeneous graph learning. Nature Communications, 2024. DOI: 10.1038/s41467-024-49171-7. https://www.nature.com/articles/s41467-024-49171-7

**C3 · stClinic** — stClinic dissects clinically relevant niches by integrating spatial multi-slice multi-omics data in dynamic graphs. Nature Communications, 2025. DOI: 10.1038/s41467-025-60575-x. https://www.nature.com/articles/s41467-025-60575-x

**J1 · DeepST** — DeepST: identifying spatial domains in spatial transcriptomics by deep learning. Nucleic Acids Research, 2022. DOI: 10.1093/nar/gkac901. https://academic.oup.com/nar/article/50/22/e131/6761985

**J2 · DeepCCI** — DeepCCI: a deep learning framework for identifying cell–cell interactions from single-cell RNA sequencing data. Bioinformatics, 2023. DOI: 10.1093/bioinformatics/btad596. https://academic.oup.com/bioinformatics/article/39/10/btad596/7281356

**J3 · DeepTalk** — Deciphering cell–cell communication at single-cell resolution for spatial transcriptomics with subgraph-based graph attention network. Nature Communications, 2024. DOI: 10.1038/s41467-024-51329-2. https://www.nature.com/articles/s41467-024-51329-2

