"""Execute a user-filled local manifest; never install, download, or invoke a shell.
Exit-code success is NOT scientific reproduction. Review argv and source before use.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, subprocess, sys
import yaml

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''): h.update(block)
    return h.hexdigest()

def validate(config: dict) -> None:
    if not isinstance(config, dict): raise ValueError('Manifest must be a mapping')
    for field in ['paper_id','figure_panel','upstream_version_or_commit','working_directory']:
        if not config.get(field): raise ValueError(f'Missing {field}')
    if config.get('status') != 'ready_for_local_execution':
        raise ValueError('Review configuration and explicitly set status: ready_for_local_execution')
    argv=config.get('command')
    if not isinstance(argv,list) or not argv or not all(isinstance(x,str) and x for x in argv):
        raise ValueError('command must be a nonempty argv list')
    if not Path(config['working_directory']).is_dir(): raise ValueError('Missing working directory')
    if not config.get('inputs'): raise ValueError('Declare at least one local input and hash')
    for item in config['inputs']:
        p=Path(item['path'])
        if not p.is_file() or sha256(p)!=item.get('sha256'): raise ValueError(f'Input mismatch: {p}')
    if not config.get('expected_outputs'): raise ValueError('Declare expected outputs')
    for name in config['expected_outputs']:
        if not isinstance(name,str) or not name: raise ValueError('Invalid output path')
        p=Path(name)
        if not p.is_absolute(): p=Path(config['working_directory'])/p
        if p.exists(): raise ValueError(f'Output already exists; use a fresh run directory: {p}')
    timeout=config.get('timeout_seconds',3600)
    if not isinstance(timeout,int) or timeout <= 0: raise ValueError('Invalid timeout')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest',type=Path)
    parser.add_argument('--output',type=Path,required=True,help='New, nonexistent log directory')
    args=parser.parse_args()
    cfg=yaml.safe_load(args.manifest.read_text())
    validate(cfg)
    args.output.mkdir(parents=True,exist_ok=False)
    start=datetime.now(timezone.utc).isoformat()
    completed=None;error=None
    try:
        with (args.output/'stdout.log').open('w') as out,(args.output/'stderr.log').open('w') as err:
            completed=subprocess.run(cfg['command'],cwd=cfg['working_directory'],shell=False,
                                     stdout=out,stderr=err,timeout=cfg.get('timeout_seconds',3600))
    except (OSError,subprocess.TimeoutExpired) as exc: error=str(exc)
    outputs=[]
    for name in cfg['expected_outputs']:
        p=Path(name)
        if not p.is_absolute(): p=Path(cfg['working_directory'])/p
        outputs.append({'path':str(p),'exists':p.is_file(),'sha256':sha256(p) if p.is_file() else None})
    rec={'started_at_utc':start,'finished_at_utc':datetime.now(timezone.utc).isoformat(),
         'manifest':cfg,'python':sys.version,'returncode':None if completed is None else completed.returncode,
         'error':error,'outputs':outputs,'scientific_acceptance':'NOT_ASSESSED'}
    (args.output/'execution.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2))
    if error or completed is None or completed.returncode!=0 or not all(x['exists'] for x in outputs):
        raise SystemExit(1)
    print('Command completed; scientific acceptance remains NOT_ASSESSED.')
if __name__=='__main__': main()
