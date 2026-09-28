"""Package/contract QA, NOT validation of agent behavior or biological accuracy."""
from pathlib import Path
import ast, hashlib, json, re, subprocess, sys
import numpy as np
import nbformat
import pytest
import yaml
from lab.statistics import pseudobulk_counts
from workflows.run_reproduction import validate
ROOT=Path(__file__).resolve().parents[1]

def read_json(name): return json.loads((ROOT/name).read_text())

def test_skill_inventory_and_version():
    reg=read_json('references/skill_registry.json')
    assert len(reg)==28 and len({x['slug'] for x in reg})==28
    for row in reg:
        txt=(ROOT/'skills'/row['slug']/'GUIDE.md').read_text()
        assert 'version: 0.2.0' in txt
        for heading in ['触发','输入','步骤','分支','验收','失败','输出']:
            assert heading in txt

def test_sources_unique_and_honest_depth():
    src=read_json('references/gap_sources.json')
    assert len(src)==35 and len({x['id'] for x in src})==35
    for x in src:
        assert x['url'].startswith('https://')
        assert x['checked_scope'] and x['reading_depth'] and x['limitations']
        assert x['downloaded_to_package'] is False

def test_original_paper_reproduction_not_promoted():
    rows=read_json('audits/paper_reproduction_matrix.json')
    assert len(rows)==20
    assert all(not r['original_figure_reproduced'] and not r['upstream_source_executed'] for r in rows)
    assert all(not r['full_supplement_read'] for r in rows)

def test_agent_behavior_cases_remain_unexecuted():
    cases=read_json('evaluations/cases.json')
    assert len(cases)==38 and len({x['id'] for x in cases})==38
    assert all(x['execution_status']=='not_run' and x['observed_response'] is None for x in cases)

def test_local_markdown_links_exist():
    errors=[]
    for file in ROOT.rglob('*.md'):
        if 'history' in file.parts or '.pytest_cache' in file.parts: continue
        text=re.sub(r'```.*?```','',file.read_text(),flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if target.startswith(('http:','https:','mailto:','#')): continue
            target=target.split('#')[0]
            if target and not (file.parent/target).exists(): errors.append((str(file.relative_to(ROOT)),target))
    assert not errors,errors

def test_yaml_contracts_remain_explicitly_unfilled():
    files=list((ROOT/'workflows').glob('*.yaml'))
    assert len(files)==8
    for f in files:
        cfg=yaml.safe_load(f.read_text())
        assert cfg['schema_version']==1 and cfg['status']=='requires_project_values'

def test_reproduction_manifest_rejected_until_filled():
    cfg=yaml.safe_load((ROOT/'workflows/reproduction_manifest.yaml').read_text())
    with pytest.raises(ValueError): validate(cfg)

def test_all_python_parses():
    for f in ROOT.rglob('*.py'): ast.parse(f.read_text(),filename=str(f))

def test_notebooks_executed_without_errors():
    files=list((ROOT/'notebooks').glob('*.ipynb'))
    assert len(files)==6
    for f in files:
        nb=nbformat.read(f,as_version=4)
        nbformat.validate(nb)
        code=[c for c in nb.cells if c.cell_type=='code']
        assert len(code)>=3 and all(c.execution_count is not None for c in code)
        assert not any(o.output_type=='error' for c in code for o in c.outputs)
    assert len(read_json('results/notebook_execution.json'))==6

def test_synthetic_results_scope_and_oracles():
    report=read_json('results/execution_report.json')
    assert report['original_paper_reproductions']==0 and len(report['experiments'])==6
    r=report['experiments']
    assert all(x['oracle_max_plan_abs_error']<1e-6 for x in r['optimal_transport']['unbalanced'])
    assert r['flow_matching']['paired_endpoint_RMSE']<.03
    assert set(report['optional_upstream_runtime'].values())=={'not_run_missing_dependency'}

def test_missing_groups_rejected():
    with pytest.raises(ValueError): pseudobulk_counts([[1],[2]],['donor',''])
    with pytest.raises(ValueError): pseudobulk_counts([[1],[2]],np.array(['donor',None],dtype=object))

def test_count_overflow_rejected_before_int64_addition():
    with pytest.raises(OverflowError):
        pseudobulk_counts(np.array([[2**62],[2**62]],dtype=np.int64),['d','d'])

def test_local_reproduction_executor_records_scope(tmp_path):
    inp=tmp_path/'input.txt';inp.write_text('synthetic local executor test')
    out=tmp_path/'answer.txt'
    cfg={'status':'ready_for_local_execution','paper_id':'SYNTHETIC_EXECUTOR_TEST',
         'figure_panel':'none','upstream_version_or_commit':'test-only-not-a-paper-commit',
         'working_directory':str(tmp_path),
         'inputs':[{'path':str(inp),'sha256':hashlib.sha256(inp.read_bytes()).hexdigest()}],
         'command':[sys.executable,'-c',"from pathlib import Path; Path('answer.txt').write_text('42')"],
         'expected_outputs':[str(out)],'timeout_seconds':20}
    cfgfile=tmp_path/'test.yaml';cfgfile.write_text(yaml.safe_dump(cfg))
    p=subprocess.run([sys.executable,'-m','workflows.run_reproduction',str(cfgfile),'--output',str(tmp_path/'logs')],
                      cwd=ROOT,text=True,capture_output=True,timeout=30)
    assert p.returncode==0,p.stderr
    ans=json.loads((tmp_path/'logs'/'execution.json').read_text())
    assert ans['scientific_acceptance']=='NOT_ASSESSED' and ans['returncode']==0
    assert out.read_text()=='42'
    with pytest.raises(ValueError): validate(cfg) # do not reuse stale outputs

def test_source_audit_does_not_claim_pinned_mutable_source():
    data=read_json('audits/source_audit.json')
    assert all(not x['runtime_executed'] for x in data['entries'])
    assert all(x['source_commit'] is None for x in data['entries'])
