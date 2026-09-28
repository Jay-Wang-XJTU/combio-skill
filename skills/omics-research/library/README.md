# 单细胞与空间组学计算方法研究开发技能库

**v0.2.0 · 2026-09-28 · 文献驱动、定向源码审计、有限范围数值验证。**

本版在用户提供的v0.1上直接更新：保留20张原论文证据卡与原20个技能，新增8个专项技能、7章知识、35条新增来源记录、8份工作流配置、6个已执行Notebook及数值测试。

**没有完成全部20篇原论文的原数据/原图复现，也没有完整核读它们所有SI。** 本轮运行的是自己的六个合成/数值实验；64项数值/结构测试通过；POT、Meta flow_matching、moscot和NicheCompass官方软件未运行。38个agent行为案例尚未执行。具体状态见[升级报告](UPGRADE_REPORT_ZH.md)、[缺口状态](coverage_gaps.md)和[执行报告](results/execution_report.json)。

## 从这里开始

先读[总路由](GUIDE.md)，根据当前项目阶段加载少数相关技能；定题始终先于挑模型。新补内容可按[阅读路线](LEARNING_PATH_ZH.md)学习。原20篇知识保留在[原文献知识总报告](KNOWLEDGE_BASE_ZH.md)；本轮新增来源、阅读范围及访问限制在[来源索引](references/GAP_SOURCES.md)。

```text
omics_skill_research/
  GUIDE.md                   总路由
  AGENTS.md                  科研工作区证据与执行约束
  skills/                    28个独立GUIDE.md
  papers/                    20张原论文证据卡
  knowledge/                 7章专项知识
  references/                原20篇+新增35条来源登记，来源不是全部全文读完
  audits/                    SI/源码审计与逐篇未完成复现矩阵
  workflows/                 8份配置、受控执行器、未执行edgeR模板
  lab/                       本地独立教育性实现
  notebooks/                 6份保存实际输出的Notebook
  tests/                     数值与结构检查
  results/                   实际环境、JSON结果、日志、测试报告
  evaluations/               38个尚未执行的agent行为案例
  templates/                 原项目模板
  history/                   v0.1历史声明，非当前状态
```

## 用作技能库

把本文件夹作为项目内可读知识目录，先让agent读取`AGENTS.md`与根`GUIDE.md`。具体agent的插件格式/发现机制可能不同；本包没有验证所有平台的自动安装。不要把28个技能无差别灌入同一上下文，按问题路由并保留相对目录。

## 运行代码

在独立Python环境审查并安装所需依赖后，从包根目录：

```bash
python -m lab.run_all
python -m pytest -q tests --junitxml=results/pytest.xml
```

脚本会重写对应的results文件，需保留本版运行记录时先复制。`requirements-tested.txt`是本轮已安装版本快照，不是跨平台安装保证；没有自动联网、自动安装或远程执行。详见[lab说明](lab/README.md)。

## 四类证据不可互换

F=有来源定位的文献/源码事实；S=带前提的综合决策；P=拟开展的项目验证；E=本轮实际执行并留有结果的检查。E也必须注明对象：本地数值测试不提升为原论文复现或真实生物学证据。

访问日期不替代版本/commit。论文全文、图片和第三方源码未再分发；正式应用需引用原始研究并遵守各自许可。Source IDs、阅读范围与未运行状态是科学交付的一部分，不得为显得完整而删除。
