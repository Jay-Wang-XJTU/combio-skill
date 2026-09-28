#!/usr/bin/env python3
"""Offline native-skill installer. Shared router is always included.

Requires Python 3.8+. No pip/R/CUDA installation, training, network, hooks,
project AGENTS.md edits or automatic overwrites. Use --update explicitly.
"""
import argparse
import datetime
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
from common import ROOT, OWNER, read_json, write_json, inventory, assert_no_symlink, check_tree
from validate_repo import validate


def destination(args):
    if args.dest:
        if args.project or args.scope!='user':
            raise ValueError('--dest cannot be combined with project scope')
        return Path(os.path.abspath(os.path.expanduser(args.dest)))
    if args.scope=='project':
        if not args.project or not Path(args.project).expanduser().is_dir():
            raise ValueError('Project scope requires an existing --project directory')
        return Path(os.path.abspath(os.path.expanduser(args.project)))/'.agents/skills'
    if args.project:
        raise ValueError('--project requires --scope project')
    return Path.home()/'.agents/skills'


def choose(args, cat):
    selected={'omics-research'}
    ids={str(r['id']):n for n,r in cat['skills'].items()}
    if args.only:
        for item in args.only:
            name=ids.get(item,item)
            if name not in cat['skills']: raise ValueError('Unknown skill: '+item)
            selected.add(name)
    else:
        selected.update(ids[str(n)] for n in cat['profiles'][args.profile])
    return selected


def load_owned(path, allowed):
    if not path.exists(): return None
    if path.is_symlink(): raise ValueError('Manifest is symlinked')
    old=read_json(path)
    if old.get('owner')!=OWNER or not isinstance(old.get('skills'),dict):
        raise ValueError('Unrecognized ownership manifest')
    if not set(old['skills']).issubset(allowed): raise ValueError('Unsafe manifest names')
    return old


def run(args):
    cat=read_json(ROOT/'catalog.json')
    if args.list:
        return {'profiles':cat['profiles'],'skills':list(cat['skills'])}
    dest=destination(args)
    state=dest.parent/'omics-method-research-github'
    assert_no_symlink(dest);assert_no_symlink(state)
    manifest=state/'install-manifest.json'
    old=load_owned(manifest,set(cat['skills']))
    if args.check:
        if old is None: raise ValueError('No installation managed by this installer')
        return dict(check_tree(dest,old['skills']),status='CHECK_OK',destination=str(dest))
    validate()
    selected=choose(args,cat)
    legacy=None
    if args.migrate_v02:
        if old: raise ValueError('Already migrated; use --update, not --migrate-v02')
        legacy_path=dest.parent/'omics-method-research/install-manifest.json'
        assert_no_symlink(legacy_path)
        legacy=read_json(legacy_path)
        if legacy.get('owner')!='omics-method-research-codex-adapter':
            raise ValueError('Unrecognized legacy manifest; refusing migration')
        if not set(legacy.get('skills',{})).issubset(cat['skills']):
            raise ValueError('Unsafe legacy skill names')
        for name,item in legacy['skills'].items():
            if inventory(dest/name)!=item['files']:
                raise ValueError('Legacy skill was edited; preserve and review it: '+name)
        selected.update(legacy['skills'])
    if old:
        check_tree(dest,old['skills'])  # Never overwrite manually edited managed files.
        selected.update(old['skills'])
    known=set(old['skills']) if old else set(legacy['skills']) if legacy else set()
    for name in selected:
        target=dest/name
        if target.is_symlink(): raise ValueError('Existing skill is symlinked; choose one installation manager')
        if target.exists() and name not in known:
            raise ValueError('Unmanaged skill collision; preserved: '+str(target))
    source=read_json(ROOT/'SKILLS_SHA256.json')['skills']
    desired={'owner':OWNER,'version':cat['distribution_version'],
             'skills':{n:source[n] for n in sorted(selected)},'codex_runtime_tested':False}
    if old==desired:
        return {'status':'UP_TO_DATE','skills':len(selected),'destination':str(dest)}
    if old and not args.update: raise ValueError('Existing installation; use --update to add/update skills')
    plan={'skills':sorted(selected),'destination':str(dest),'knowledge_version':cat['knowledge_version']}
    if args.dry_run: return dict(plan,status='DRY_RUN',writes_performed=False)
    state.mkdir(parents=True,exist_ok=True)
    lock=state/'.install-lock'
    try: lock.mkdir()
    except FileExistsError: raise ValueError('Installation lock exists; another install may be running')
    stage=None;moved=[];committed=[]
    backup=state/'backups'/datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    try:
        dest.mkdir(parents=True,exist_ok=True)
        stage=Path(tempfile.mkdtemp(prefix='.stage-',dir=str(state)))
        for name in sorted(selected):
            shutil.copytree(ROOT/'skills'/name,stage/name)
        check_tree(stage,desired['skills'])
        write_json(stage/'install-manifest.json',desired)
        targets=[(stage/n,dest/n,'skills/'+n) for n in sorted(selected)]
        targets.append((stage/'install-manifest.json',manifest,'install-manifest.json'))
        for source_path,target,label in targets:
            if target.exists():
                if target!=manifest and target.name not in known:
                    raise ValueError('Unexpected target appeared: '+str(target))
                saved=backup/label;saved.parent.mkdir(parents=True,exist_ok=True)
                target.rename(saved);moved.append((saved,target))
            source_path.rename(target);committed.append(target)
        check_tree(dest,desired['skills'])
    except Exception:
        for target in reversed(committed):
            if target.is_dir():shutil.rmtree(target)
            elif target.exists():target.unlink()
        for saved,target in reversed(moved):saved.rename(target)
        raise
    finally:
        if stage is not None: shutil.rmtree(stage,ignore_errors=True)
        lock.rmdir()
    return dict(plan,status='INSTALLED',backup=str(backup) if moved else None,
                legacy_library_preserved=bool(legacy),codex_runtime_tested=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--scope',choices=['user','project'],default='user')
    p.add_argument('--project');p.add_argument('--dest')
    p.add_argument('--profile',choices=list(read_json(ROOT/'catalog.json')['profiles']),default='all')
    p.add_argument('--only',nargs='+')
    g=p.add_mutually_exclusive_group()
    g.add_argument('--check',action='store_true');g.add_argument('--list',action='store_true')
    g.add_argument('--dry-run',action='store_true')
    p.add_argument('--update',action='store_true');p.add_argument('--migrate-v02',action='store_true')
    args=p.parse_args()
    try: print(json.dumps(run(args),ensure_ascii=False,indent=2));return 0
    except (ValueError,OSError,KeyError) as e: print('ERROR: '+str(e),file=sys.stderr);return 1

if __name__=='__main__':sys.exit(main())
