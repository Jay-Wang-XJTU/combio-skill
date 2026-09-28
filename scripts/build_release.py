#!/usr/bin/env python3
"""Build a deterministic source archive from the explicit release-file allowlist."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile
from common import ROOT, read_json


def build(output=None):
    listing=read_json(ROOT/'RELEASE_FILES.json')['files']
    output=Path(output) if output else ROOT/'dist/omics-method-research-skills-v0.2.1.zip'
    output.parent.mkdir(parents=True,exist_ok=True)
    members=listing+['RELEASE_FILES.json']
    for rel in members:
        p=ROOT/rel
        if p.is_symlink() or not p.is_file():raise ValueError('Missing/unsafe release member: '+rel)
        if rel in listing and hashlib.sha256(p.read_bytes()).hexdigest()!=read_json(ROOT/'RELEASE_FILES.json')['sha256'][rel]:
            raise ValueError('Release hash differs; review before refreshing manifest: '+rel)
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for rel in sorted(members):
            info=zipfile.ZipInfo('omics-method-research-skills/'+rel,date_time=(2026,9,28,0,0,0))
            info.external_attr=0o100644<<16;info.compress_type=zipfile.ZIP_DEFLATED
            z.writestr(info,(ROOT/rel).read_bytes())
    digest=hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(output.suffix+'.sha256').write_text(digest+'  '+output.name+'\n',encoding='utf-8')
    return {'archive':str(output),'sha256':digest,'files':len(members)}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output')
    a=p.parse_args();print(json.dumps(build(a.output),indent=2))
