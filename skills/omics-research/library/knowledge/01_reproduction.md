# 01｜补充材料—源码—论文结果：怎样建立可复现证据

**定位：**这是方法开发中的审计技能，不把“读过论文”“运行成功”和“重现生物学结论”混成一个状态。本轮取得了 NicheCompass 完整44页SI的网页访问，并定向核查其补充方法；没有逐页逐图完成全部SI审计，没有运行原始生物学数据。[G19](../references/GAP_SOURCES.md#g19--nichecompass-supplementary-information)

## 1. 用正交证据字段，而非一个“完成”标签

每个主张单独记录：正文/补充材料读到何处；源文件与函数是否核查；依赖版本是否锁定；原始输入是否获取且校验；单元/数值检查是否运行；作者示例是否运行；原论文图表是否重现；独立数据是否支持。源码核查不能自动把其所有实验升级为复现成功；toy数值验证也不能替代原论文证据。

文件、图表和主张之间建立对应：`claim_id → paper figure/table → supplement section/page → repository/ref/file/function → data accession/hash → command/config → raw output → metric → decision`。任何缺项保留null及原因。没有信息时禁止填“默认参数”或猜commit。

## 2. 阅读完整SI的执行法

先列出全部附加文件，不只一个PDF：SI正文、Supplementary Tables、Source Data、Reporting Summary、Protocol、视频以及更正。建立每个图/表/注释的coverage行，状态分为located、text_read、image_inspected、method_traced、result_reproduced。扫描图或公式必须看页图。阅读每个实验时提取任务、独立单位、标签/先验来源、数据排除、样本量、训练预算、失败处理及不确定性。

优先读决定主张成立的实验，但“定向阅读”必须显式标注。下载完整文件不等于完整阅读；看完所有正文页也不等于审计其每个结论。完整SI验收需要图表清单无未解释遗漏，且关键实验可追到实现。该条件对本轮20篇论文仍未全部满足。

## 3. 这次发现的三个具体审计对象

NicheCompass SI物理页41的差异活性量包含高斯后验比较概率，不能因为记作p就直接套BH；页42的模拟程序比较使用与模拟真值一致的邻域范围，并按真实上调程序数量截取排名。这支持对应的受控设置，但不是未知邻域/未知程序数量的一般证明。页42–43的指标聚合有比较集合相关的缩放步骤，新增baseline时应检查综合分数的相对性。[G19](../references/GAP_SOURCES.md#g19--nichecompass-supplementary-information)

发表分析环境与今天的软件环境也不是一回事。NicheCompass分别给出软件归档 `10.5281/zenodo.14621258` 和分析归档 `10.5281/zenodo.14632687`；stClinic给出发表时环境和归档 `https://zenodo.org/records/15246396`。应分别锁定，不能仅clone最新main替代。[G20、G21](../references/GAP_SOURCES.md)

源码里的默认值会改变目标函数。POT文档记录0.9.5起UOT默认正则从entropy改为KL；本包把正则参考测度写入配置，并用独立优化器验证自己的实现。**这不是运行POT官方包。**[G17、G18](../references/GAP_SOURCES.md)

## 4. 从最小可复现单元到论文级重现

第一步：建立干净隔离环境，记录Python/R、操作系统、CPU/GPU、BLAS/CUDA、依赖锁文件和仓库commit。不要在用户主环境随意降级包。依赖失败保留完整日志；修补以后另记patch版本，不能继续声称原环境未改。

第二步：验证数据契约。核对raw counts、gene IDs、cells/spot顺序、坐标单位、图方向、标签与split。校验表格尺寸和hash；禁止悄悄下载“看起来相似”的另一数据版本。公开数据仍要遵循许可，受控患者数据不放进skill包。

第三步：做公式/函数微复现。先验证边界条件、形状、方向、尺度和停止准则，再跑作者最小教程。两种验证分开记录。本包Gaussian后验比较、KL-UOT与CFM实验属于此层级。

第四步：在一个预先选定的数据子集重现单个主图的数值。明确图中的实验到底使用了几位患者、几张切片、多少seed；使用相同任务、同等先验、同一评价单位。定量比较应包含数据数量、效应方向、效应大小、误差条、运行失败率；不要求随机UMAP像素完全一致。

第五步：完整benchmark和新数据复核。复现成功的验收容差要事前由数值精度、随机性和科学上有意义的差异来规定，而不是看结果后放宽。保留不一致结果，不用挑seed修复结论。

## 5. 失败分类与修复决策

下载失败→保留URL/日期/错误并标blocked_access；依赖冲突→保留原环境要求与新环境差异；数值不稳定→检查浮点精度、log域、cost单位与收敛；结果不一致→先查数据/版本/指标定义，再查随机性。若必须改算法，报告的是适配版，不是原样重现。

`audits/paper_reproduction_matrix.json`覆盖原包20篇的当前状态；`workflows/reproduction_manifest.yaml`是执行合同。未知的具体作者脚本入口保留待定位，不伪造可执行命令。

## 6. 交付与许可

本包分发自写说明和实验，不打包论文PDF、第三方整库或用户受控数据。官方Meta源码头部有其自身许可约束；本包根据数学定义独立实现路径采样，没有复制整份源码。引用与可访问不等于有再分发许可。[G25](../references/GAP_SOURCES.md)

验收产物：coverage清单、source audit、环境与输入hash、原命令和日志、结构化数值差异、失败记录以及允许使用的结论。工具返回“exit code 0”只完成运行层面的验收。
