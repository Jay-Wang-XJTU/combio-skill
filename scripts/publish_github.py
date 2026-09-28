#!/usr/bin/env python3
"""Create a NEW GitHub repository from an audited allowlist.

Default is a no-network/no-write preview. --execute requires configured git/gh,
explicit owner/repo, and explicit visibility. Existing repositories are refused.
--release additionally uploads the archive to a DRAFT GitHub Release.
Never asks for tokens, changes visibility, overwrites an existing repo, or force-pushes.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from common import ROOT, read_json
from validate_repo import validate
from build_release import build


def invoke(argv,cwd=None):
    p=subprocess.run(argv,cwd=cwd,text=True,capture_output=True,timeout=180)
    if p.returncode:
        raise RuntimeError('Command failed: '+' '.join(argv)+'\n'+p.stderr.strip())
    return p.stdout.strip()


def plan(repo,visibility,release=False):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9][A-Za-z0-9_.-]*',repo):
        raise ValueError('Use OWNER/REPO, not a URL or token')
    if visibility not in ('private','public'):raise ValueError('Select private or public')
    return {'status':'DRY_RUN','repo':repo,'visibility':visibility,'create_only':True,
            'upload_source_tree':True,'upload_zip_as_draft_release':release,
            'commands':[
              ['gh','auth','status'],
              ['git','init','-b','main','<fresh-staging-directory>'],
              ['git','add','--','<explicit-release-file-allowlist>'],
              ['git','commit','-m','Release omics research skills distribution v0.2.1'],
              ['gh','repo','create',repo,'--'+visibility,'--source','<fresh-staging-directory>',
               '--remote','origin','--push']],
            'writes_performed':False}


def execute(args):
    p=plan(args.repo,args.visibility,args.release)
    validate()
    allow=read_json(ROOT/'RELEASE_FILES.json')
    for rel in allow['files']:
        f=ROOT/rel
        if f.is_symlink() or not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=allow['sha256'][rel]:
            raise ValueError('Release allowlist mismatch: '+rel)
    if not args.execute:return p
    for command in ['git','gh']:
        if not shutil.which(command):raise ValueError('Missing '+command+'; install and authenticate it on your own machine')
    invoke(['gh','auth','status'])
    probe=subprocess.run(['gh','repo','view',args.repo,'--json','nameWithOwner'],text=True,capture_output=True,timeout=60)
    if probe.returncode==0:
        raise ValueError('Repository already exists; no upload performed. Use reviewed branch/PR workflow in docs/PUBLISH_ZH.md')
    # A failed existence probe is not proof of absence. The create-only API below
    # is the final collision check, and never edits an existing repository.
    work=ROOT/'.local';work.mkdir(exist_ok=True)
    staging=Path(tempfile.mkdtemp(prefix='publish-',dir=str(work)))
    for rel in allow['files']+['RELEASE_FILES.json']:
        dst=staging/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/rel,dst)
    print('Staging retained at: '+str(staging),file=sys.stderr)
    invoke(['git','init','-b','main'],staging)
    invoke(['git','var','GIT_AUTHOR_IDENT'],staging) # refuses unconfigured identity
    invoke(['git','add','--',*allow['files'],'RELEASE_FILES.json'],staging)
    invoke(['git','commit','-m','Release omics research skills distribution v0.2.1'],staging)
    invoke(['gh','repo','create',args.repo,'--'+args.visibility,'--source',str(staging),
            '--remote','origin','--push'],staging)
    repo_info=json.loads(invoke(['gh','repo','view',args.repo,'--json','url,isPrivate'],staging))
    result={'status':'SOURCE_PUSHED','repository':repo_info,'staging':str(staging),
            'commit':invoke(['git','rev-parse','HEAD'],staging)}
    if args.release:
        artifact=build()
        invoke(['git','tag','v0.2.1'],staging)
        invoke(['git','push','origin','refs/tags/v0.2.1'],staging)
        invoke(['gh','release','create','v0.2.1',artifact['archive'],artifact['archive']+'.sha256',
                '--repo',args.repo,'--verify-tag','--draft','--title','Omics research skills v0.2.1',
                '--notes-file',str(ROOT/'docs/RELEASE_NOTES.md')],staging)
        result['draft_release_created']=True
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',required=True);p.add_argument('--visibility',required=True,choices=['private','public'])
    p.add_argument('--execute',action='store_true');p.add_argument('--release',action='store_true')
    a=p.parse_args()
    try:print(json.dumps(execute(a),ensure_ascii=False,indent=2))
    except (ValueError,OSError,RuntimeError,subprocess.TimeoutExpired) as e:
        print('ERROR: '+str(e),file=sys.stderr);sys.exit(1)
