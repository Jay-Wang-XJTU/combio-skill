# Research-skill workspace contract

先读README.md、GUIDE.md、coverage_gaps.md和当前任务对应skill。按需加载知识章与来源，不一次把所有论文当统一事实。

状态必须可审计：F=来源中的事实；S=跨文献综合；P=待检验建议；E=本包真实执行产物。它们不是同一证据等级。

执行前先审查数据权限、独立单位、训练测试边界、测量链和目标量。不要自动修改用户主环境，不触碰不相关数据，不静默升级依赖，不上传受控数据。

数值实验命令：`python -m lab.run_all`。测试命令：`python -m pytest tests -q`。它们不下载原论文数据，也不执行不明远程脚本。运行后分别记录数值测试、agent行为评测、官方软件运行和原图复现状态。

禁止推断：seed是生物学重复；后验概率就是p值；BY修复所有偏差；表达相近就是祖先后代；CondOTProbPath会自己求OT；UOT归一后普通FM自动处理质量；分割marker更纯就是独立真值；所有潜变量可解释；跑通toy等于复现Nature论文。

当前20篇原文没有完成全部SI和原数据重跑；具体看audits/paper_reproduction_matrix.json。未取得的版本/hash必须保留null；未来更新不得删除失败记录。
