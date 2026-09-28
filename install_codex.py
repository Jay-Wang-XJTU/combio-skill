#!/usr/bin/env python3
"""Convenience entry point for the offline installer."""
from pathlib import Path
import runpy
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'scripts'))
runpy.run_path(str(HERE/'scripts/install_codex.py'),run_name='__main__')
