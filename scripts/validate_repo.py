#!/usr/bin/env python3
"""Validate release content, entry points, relative dependencies and provenance."""
from pathlib import Path
import ast
import hashlib
import json
import re
import sys
from common import ROOT, read_json, check_tree, inventory


def validate(root=ROOT):
    root=Path(root)
    cat=read_json(root/'catalog.json')['skills']
    expected=read_json(root/'SKILLS_SHA256.json')['skills']
    actual={p.name for p in (root/'skills').iterdir() if p.is_dir()}
    if actual != set(cat) or set(expected) != set(cat) or len(cat) != 29:
        raise ValueError('Expected exactly 29 public skill folders')
    result=check_tree(root/'skills', expected)
    discovered=list((root/'skills').rglob('SKILL.md'))
    if len(discovered)!=29:
        raise ValueError('Ambiguous recursive skill discovery')
    lib=root/'skills/omics-research/library'
    provenance=read_json(root/'provenance/library_transform.json')['files']
    if len(provenance)!=133 or len(inventory(lib))!=133:
        raise ValueError('Scientific library file count changed')
    for row in provenance:
        p=lib/row['distributed_path']
        if hashlib.sha256(p.read_bytes()).hexdigest()!=row['distributed_sha256']:
            raise ValueError('Provenance mismatch: '+row['distributed_path'])
    link_errors=[]
    for f in lib.rglob('*.md'):
        if 'history' in f.relative_to(lib).parts: continue
        text=re.sub(r'```.*?```','',f.read_text(encoding='utf-8'),flags=re.S)
        for link in re.findall(r'\]\(([^)]+)\)',text):
            if link.startswith(('http:', 'https:', 'mailto:', '#')): continue
            link=link.split('#')[0]
            if link and not (f.parent/link).exists():
                link_errors.append(str(f.relative_to(lib))+' -> '+link)
    if link_errors: raise ValueError('Broken library links: '+repr(link_errors))
    for p in root.rglob('*.py'):
        if '.local' not in p.parts:
            ast.parse(p.read_text(encoding='utf-8'), filename=str(p))
    native=read_json(root/'plugin.json')
    compat=read_json(root/'.codex-plugin/plugin.json')
    market=read_json(root/'.agents/plugins/marketplace.json')
    if native['version']!=compat['version'] or native['name']!=compat['name']:
        raise ValueError('Plugin manifests disagree')
    if market['plugins'][0]['source']['path']!='./':
        raise ValueError('Marketplace must package this repository root')
    # Conservative token patterns: useful guard, not a guarantee of no sensitive data.
    token_re=re.compile(r'gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{30,}|-----BEGIN (?:OPENSSH|RSA|EC) PRIVATE KEY-----')
    for base in (root/'skills',root/'docs'):
        for p in base.rglob('*'):
            if p.is_file() and token_re.search(p.read_text(encoding='utf-8',errors='ignore')):
                raise ValueError('Potential secret; review before publishing: '+str(p))
    return dict(result,status='REPOSITORY_OK',scientific_experiments_rerun=False,
                library_markdown_links_checked_excluding_history=True)

if __name__=='__main__':
    try: print(json.dumps(validate(),ensure_ascii=False,indent=2))
    except (ValueError,OSError,KeyError) as e:
        print('ERROR: '+str(e),file=sys.stderr);sys.exit(1)
