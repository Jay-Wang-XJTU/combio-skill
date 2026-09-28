"""Shared stdlib-only deployment helpers. No network or scientific execution."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OWNER = 'omics-method-research-github-v1'


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_json(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def inventory(root):
    root = Path(root)
    if not root.is_dir() or root.is_symlink():
        raise ValueError('Expected a real directory: '+str(root))
    out = {}
    for p in sorted(root.rglob('*')):
        if p.is_symlink():
            raise ValueError('Symlink in managed content: '+str(p))
        if p.is_file():
            out[p.relative_to(root).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def assert_no_symlink(path):
    path = Path(path).absolute()
    for parent in (path, *path.parents):
        if parent.is_symlink():
            raise ValueError('Refusing symlinked destination component: '+str(parent))


def check_tree(skills, expected=None):
    """Check public wrappers, dependency paths, and optionally all file hashes."""
    skills = Path(skills)
    if expected is None:
        names = sorted(p.parent.name for p in skills.glob('omics-*/SKILL.md'))
    else:
        names = sorted(expected)
    if not names:
        raise ValueError('No omics skills found at '+str(skills))
    if 'omics-research' not in names:
        raise ValueError('Missing required omics-research shared-library bundle')
    for name in names:
        if not re.fullmatch(r'omics-[a-z0-9-]+', name):
            raise ValueError('Unsafe skill name')
        folder = skills/name
        text = (folder/'SKILL.md').read_text(encoding='utf-8')
        match = re.search(r'^name:\s*(.+)$', text, re.M)
        if not match or match.group(1).strip().strip('"\'') != name:
            raise ValueError('Frontmatter name mismatch: '+name)
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if link.startswith(('https:', 'http:', '#')):
                continue
            target = (folder/link.split('#')[0]).resolve()
            try: target.relative_to(skills.resolve())
            except ValueError: raise ValueError('Wrapper link escapes skill root: '+link)
            if not target.is_file():
                raise ValueError('Broken dependency: '+name+' -> '+link)
        if expected is not None and inventory(folder) != expected[name]:
            raise ValueError('Missing/changed/extra managed files in '+name)
    inner = list((skills/'omics-research/library').rglob('SKILL.md'))
    if inner:
        raise ValueError('Nested discoverable SKILL.md found in reference library')
    return {'skills':len(names), 'library_files':len(inventory(skills/'omics-research/library')),
            'native_codex_runtime_tested':False}
