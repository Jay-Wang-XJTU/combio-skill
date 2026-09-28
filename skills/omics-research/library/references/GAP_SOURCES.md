# v0.2 增补来源与真实阅读范围

检索日期：2026-09-28。只收录原始论文、作者材料、官方源码/文档。新增来源条目不是“35篇全部全文阅读”。阅读深度逐项记录；未下载第三方PDF/完整源码。

## G01 · Confronting false discoveries in single-cell differential expression

来源：[Confronting false discoveries in single-cell differential expression](https://www.nature.com/articles/s41467-021-25960-2)。 DOI：`10.1038/s41467-021-25960-2`。

阅读：`abstract_and_metadata`。核查范围：生物学重复和 differential expression 基准的研究问题。

限制：本轮 Nature 正文获取失败；不声称复核全套 benchmark 或附录。

## G02 · A practical solution to pseudoreplication bias in single-cell studies

来源：[A practical solution to pseudoreplication bias in single-cell studies](https://www.nature.com/articles/s41467-021-21038-1)。 DOI：`10.1038/s41467-021-21038-1`。

阅读：`targeted_full_text`。核查范围：细胞嵌套于个体、混合模型与模拟设计。

限制：不将特定数据集的模型排序视为普遍定理。

## G03 · muscat detects subpopulation-specific state transitions from multi-sample multi-condition single-cell transcriptomics data

来源：[muscat detects subpopulation-specific state transitions from multi-sample multi-condition single-cell transcriptomics data](https://www.nature.com/articles/s41467-020-19894-4)。 DOI：`10.1038/s41467-020-19894-4`。

阅读：`abstract_and_metadata`。核查范围：多样本多条件 differential state 的任务与数据层级。

限制：未运行 muscat。

## G04 · Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing

来源：[Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing](https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1995.tb02031.x)。 DOI：`10.1111/j.2517-6161.1995.tb02031.x`。

阅读：`metadata_and_method_statement`。核查范围：BH 程序与 FDR 的原始出处。

限制：未重新完整核读原证明。

## G05 · The control of the false discovery rate in multiple testing under dependency

来源：[The control of the false discovery rate in multiple testing under dependency](https://projecteuclid.org/journals/annals-of-statistics/volume-29/issue-4/The-control-of-the-false-discovery-rate-in-multiple-testing/10.1214/aos/1013699998.short)。 DOI：`10.1214/aos/1013699998`。

阅读：`abstract_and_method_statement`。核查范围：PRDS 条件、任意依赖下 harmonic 修正。

限制：有效边际 p 值仍是前提；未审读所有证明。

## G06 · Permutation p-values should never be zero: calculating exact p-values when permutations are randomly drawn

来源：[Permutation p-values should never be zero: calculating exact p-values when permutations are randomly drawn](https://arxiv.org/abs/1603.05766)。 DOI：`10.2202/1544-6115.1585`。

阅读：`abstract_and_method_statement`。核查范围：随机置换 p 值的有限 Monte Carlo 计数。

限制：2010 论文，arXiv 链接是后续存档；穷举检验另用精确比例。

## G07 · Inference after latent variable estimation for single-cell RNA sequencing data

来源：[Inference after latent variable estimation for single-cell RNA sequencing data](https://arxiv.org/abs/2207.00554)。 DOI：`10.48550/arXiv.2207.00554`。

阅读：`abstract`。核查范围：潜变量估计后同数据检验的 double dipping；Poisson count splitting。

限制：仅按该 arXiv 版本记录；未实现专门选择性推断。

## G08 · Negative binomial count splitting for single-cell RNA sequencing data

来源：[Negative binomial count splitting for single-cell RNA sequencing data](https://arxiv.org/abs/2307.12985)。 DOI：`10.48550/arXiv.2307.12985`。

阅读：`abstract`。核查范围：Poisson thinning 在过度离散数据下不独立；NB splitting 的假设。

限制：参数估计误差及全部证明未核查。

## G09 · Causal Inference: What If — author book and companion code

来源：[Causal Inference: What If — author book and companion code](https://miguelhernan.org/whatifbook)。

阅读：`author_index_and_companion_repository`。核查范围：三部分结构、作者提供的免费代码与更新入口。

限制：2026-08-19 最新 PDF 重定向获取失败；没有宣称通读该书。

## G10 · Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines

来源：[Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines](https://www.nature.com/articles/s41592-025-02772-6)。 DOI：`10.1038/s41592-025-02772-6`。

阅读：`abstract_and_metadata`。核查范围：把强简单基线纳入扰动预测评估。

限制：结论受其测试范围限制；不是所有未来模型的普遍结论。

## G11 · Cell segmentation in imaging-based spatial transcriptomics (Baysor)

来源：[Cell segmentation in imaging-based spatial transcriptomics (Baysor)](https://www.nature.com/articles/s41587-021-01044-w)。 DOI：`10.1038/s41587-021-01044-w`。

阅读：`abstract_and_official_repository`。核查范围：分子位置、表达及形态信息用于分割。

限制：不从当前 main 推断发表版本；未执行 segmentation。

## G12 · Cell simulation as cell segmentation (Proseg)

来源：[Cell simulation as cell segmentation (Proseg)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12285883/)。 DOI：`10.1038/s41592-025-02697-0`。

阅读：`targeted_full_text`。核查范围：Introduction；Results 2.1–2.3；误分配、细胞数与伪共表达的验证限制。

限制：2025 期刊论文，区别于2024预印本；没有独立复现作者性能排名。

## G13 · SpotClean adjusts for spot swapping in spatial transcriptomics data

来源：[SpotClean adjusts for spot swapping in spatial transcriptomics data](https://pmc.ncbi.nlm.nih.gov/articles/PMC9142522/)。 DOI：`10.1038/s41467-022-30587-y`。

阅读：`targeted_full_text`。核查范围：背景spot、局部/远端污染建模、背景比例要求。

限制：适用测量机制不可无条件移植到成像式平台。

## G14 · Cell2location maps fine-grained cell types in spatial transcriptomics

来源：[Cell2location maps fine-grained cell types in spatial transcriptomics](https://www.nature.com/articles/s41587-021-01139-4)。 DOI：`10.1038/s41587-021-01139-4`。

阅读：`abstract_code_and_data_availability`。核查范围：细胞混合分解、技术变化、官方复现入口。

限制：本轮页面主体为订阅预览；不声称完整读Methods。

## G15 · Computational Optimal Transport

来源：[Computational Optimal Transport](https://arxiv.org/abs/1803.00567)。 DOI：`10.1561/2200000073`。

阅读：`abstract_author_book_index`。核查范围：OT 专题的系统入口。

限制：作者PDF约42.5MB超过网页工具大小限制；未通读书。

## G16 · Scaling Algorithms for Unbalanced Transport Problems

来源：[Scaling Algorithms for Unbalanced Transport Problems](https://arxiv.org/pdf/1607.05816)。 DOI：`10.48550/arXiv.1607.05816`。

阅读：`targeted_pdf`。核查范围：§1.3、§4.1–4.4、Algorithm 1、log-domain stabilization。

限制：47页，仅相关章节；不是全文证明审计。

## G17 · POT unbalanced API documentation

来源：[POT unbalanced API documentation](https://pythonot.github.io/gen_modules/ot.unbalanced.html)。

阅读：`targeted_official_documentation`。核查范围：目标函数、reg_type迁移、marginal relaxation、returnCost。

限制：页面标为0.9.7；本容器没有POT，官方runtime未运行。

## G18 · POT ot.unbalanced._sinkhorn rendered source

来源：[POT ot.unbalanced._sinkhorn rendered source](https://pythonot.github.io/_modules/ot/unbalanced/_sinkhorn.html)。

阅读：`targeted_source_review`。核查范围：sinkhorn_knopp_unbalanced K、fi_1/fi_2、u/v更新及cost返回。

限制：文档快照没有独立取得commit/hash；不称版本锁定复现。

## G19 · NicheCompass Supplementary Information

来源：[NicheCompass Supplementary Information](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41588-025-02120-6/MediaObjects/41588_2025_2120_MOESM1_ESM.pdf)。 DOI：`10.1038/s41588-025-02120-6`。

阅读：`targeted_supplement_pdf`。核查范围：44页PDF；重点核读物理页41–43 Supplementary Methods，截图核对41/42/43及36页。

限制：35张补图没有全部逐图审计；没有原数据重跑。

## G20 · NicheCompass source and reproducibility archives

来源：[NicheCompass source and reproducibility archives](https://www.nature.com/articles/s41588-025-02120-6)。 DOI：`10.1038/s41588-025-02120-6`。

阅读：`full_text_targeted_code_availability`。核查范围：两个不同Zenodo软件/分析归档及数据和先验依赖。

限制：归档DOI已定位，文件未下载到容器。

## G21 · stClinic full article and code availability

来源：[stClinic full article and code availability](https://www.nature.com/articles/s41467-025-60575-x)。 DOI：`10.1038/s41467-025-60575-x`。

阅读：`targeted_full_text`。核查范围：发表环境stClinic0.0.10、软件与Zenodo归档、动态图含义。

限制：SI链接尝试失败；完整SI/原数据执行仍未完成。

## G22 · Flow Matching for Generative Modeling

来源：[Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747)。 DOI：`10.48550/arXiv.2210.02747`。

阅读：`abstract`。核查范围：FM 概念与概率路径目标的原始入口。

限制：正文PDF本轮获取失败；公式另由G24正文与G25源码交叉核对。

## G23 · Flow Matching Guide and Code

来源：[Flow Matching Guide and Code](https://arxiv.org/abs/2412.06264)。 DOI：`10.48550/arXiv.2412.06264`。

阅读：`abstract_and_official_repository`。核查范围：系统学习与官方实现入口。

限制：Guide全文本轮不可读；不宣称全部定理已审读。

## G24 · Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal Transport

来源：[Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal Transport](https://arxiv.org/pdf/2302.00482)。 DOI：`10.48550/arXiv.2302.00482`。

阅读：`targeted_pdf`。核查范围：§3.1–3.2、Theorems3.1/3.2、Algorithm1、Table1、AppendixA相关证明。

限制：34页版本标记TMLR03/2024；只审读CFM/配对及其条件，不覆盖全部实验。

## G25 · Meta flow_matching/path/affine.py

来源：[Meta flow_matching/path/affine.py](https://raw.githubusercontent.com/facebookresearch/flow_matching/main/flow_matching/path/affine.py)。

阅读：`source_file_read`。核查范围：AffineProbPath.sample及CondOTProbPath；x_t和dx_t。

限制：mutable main，未取得commit/hash；CC-BY-NC来源未复制进压缩包。

## G26 · CellFlow enables generative single-cell phenotype modeling with flow matching

来源：[CellFlow enables generative single-cell phenotype modeling with flow matching](https://www.biorxiv.org/content/10.1101/2025.04.11.648220v1)。 DOI：`10.1101/2025.04.11.648220`。

阅读：`preprint_metadata_official_repository`。核查范围：Theis团队CellFlow，区别于同名其他论文。

限制：仅作为单细胞FM桥接入口，未执行或完整审读。

## G27 · CellFlow official documentation

来源：[CellFlow official documentation](https://cellflow.readthedocs.io/)。

阅读：`official_documentation_index`。核查范围：条件分布建模的使用入口。

限制：不声称原版JAX模型已在本容器复现。

## G28 · Baysor official repository

来源：[Baysor official repository](https://github.com/kharchenkolab/Baysor)。

阅读：`repository_readme`。核查范围：原作者分割实现与版本入口。

限制：main可能与原论文版本不同；没有clone/run。

## G29 · Proseg official repository

来源：[Proseg official repository](https://github.com/dcjones/proseg)。

阅读：`repository_readme`。核查范围：模型实现、输入与原论文链接。

限制：未审计所有Rust实现或执行分割。

## G30 · Using Baysor to Perform Xenium Cell Segmentation

来源：[Using Baysor to Perform Xenium Cell Segmentation](https://www.10xgenomics.com/analysis-guides/using-baysor-to-perform-xenium-cell-segmentation)。

阅读：`targeted_vendor_guide`。核查范围：示例版本、坐标与分割输入语义。

限制：历史教程，不能代表所有当前Xenium版本。

## G31 · Causal inference in statistics: An overview

来源：[Causal inference in statistics: An overview](https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf)。 DOI：`10.1214/09-SS057`。

阅读：`targeted_pdf`。核查范围：§3.3.1–3.3.3、back-door criterion与识别/估计的区别。

限制：51页，只核读相关部分；不覆盖所有因果识别算法。

## G32 · Double/debiased machine learning for treatment and structural parameters

来源：[Double/debiased machine learning for treatment and structural parameters](https://academic.oup.com/ectj/article/21/1/C1/5056401)。 DOI：`10.1111/ectj.12097`。

阅读：`targeted_full_text`。核查范围：orthogonal scores、cross-fitting、iid假设与ATE的条件。

限制：不把DML等同于自动消除未测混杂。

## G33 · DoubleML basics official documentation

来源：[DoubleML basics official documentation](https://docs.doubleml.org/stable/guide/basics.html)。

阅读：`targeted_official_documentation`。核查范围：正交化和样本分割的实践解释。

限制：本包使用自写toy估计器，不是DoubleML包复现。

## G34 · edgeR Bioconductor package and user guide entry

来源：[edgeR Bioconductor package and user guide entry](https://bioconductor.org/packages/release/bioc/html/edgeR.html)。 DOI：`10.18129/B9.bioc.edgeR`。

阅读：`official_package_index`。核查范围：NB differential expression及官方文档入口。

限制：R脚本是待运行适配模板，本容器没有执行edgeR。

## G35 · What If author-linked Python companion code

来源：[What If author-linked Python companion code](https://github.com/jrfiedler/causal_inference_python_code)。

阅读：`repository_readme`。核查范围：Part2配套Python实现入口。

限制：没有运行原书数据示例。
