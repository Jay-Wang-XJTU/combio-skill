#!/usr/bin/env python3
"""Check dependencies/hashes of this version installed by any copy-based installer."""
import argparse
import json
import sys
from pathlib import Path
from common import ROOT, read_json, check_tree
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--dest',default=str(Path.home()/'.agents/skills'))
a=p.parse_args()
try:
    dest=Path(a.dest).expanduser()
    expected=read_json(ROOT/'SKILLS_SHA256.json')['skills']
    selected={n:expected[n] for n in expected if (dest/n).is_dir()}
    print(json.dumps(dict(check_tree(dest,selected),status='CHECK_OK'),indent=2))
except (ValueError,OSError) as e: print('ERROR: '+str(e),file=sys.stderr);sys.exit(1)
