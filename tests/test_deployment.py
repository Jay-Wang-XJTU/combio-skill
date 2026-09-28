"""Deployment-only tests. No Codex model invocation, GitHub writes or biological reruns."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from common import check_tree, inventory, write_json, OWNER
from validate_repo import validate
import install_codex
from publish_github import plan
from build_release import build

class DeployTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.base=Path(self.tmp.name)
        self.dest=self.base/'.agents/skills'
    def tearDown(self):self.tmp.cleanup()
    def cli(self,*args,ok=True,dest=True):
        argv=[sys.executable,str(ROOT/'install_codex.py')]
        if dest:argv+=['--dest',str(self.dest)]
        p=subprocess.run(argv+list(args),text=True,capture_output=True,timeout=30)
        if ok:
            self.assertEqual(p.returncode,0,p.stderr)
            return json.loads(p.stdout)
        self.assertNotEqual(p.returncode,0,p.stdout)
        return p.stderr
    def test_repository_valid(self):self.assertEqual(validate()['skills'],29)
    def test_exact_recursive_discovery(self):self.assertEqual(len(list((ROOT/'skills').rglob('SKILL.md'))),29)
    def test_all_install(self):
        self.assertEqual(len(self.cli()['skills']),29)
        self.assertEqual(self.cli('--check')['library_files'],133)
    def test_router_independent(self):
        self.cli('--profile','router');self.assertEqual(check_tree(self.dest)['skills'],1)
        self.assertTrue((self.dest/'omics-research/library/skills/25-optimal-transport-theory-and-numerics/GUIDE.md').exists())
    def test_dynamic_profile(self):
        out=self.cli('--profile','dynamics')
        self.assertIn('omics-ot',out['skills']);self.assertIn('omics-flow-matching',out['skills'])
    def test_numeric_selection(self):
        out=self.cli('--only','21','25','26');self.assertEqual(len(out['skills']),4)
    def test_idempotent(self):
        self.cli();self.assertEqual(self.cli()['status'],'UP_TO_DATE')
    def test_dry_run_has_no_writes(self):
        self.assertEqual(self.cli('--dry-run')['status'],'DRY_RUN');self.assertFalse(self.dest.parent.exists())
    def test_update_required(self):
        self.cli('--profile','router');self.cli('--only','25',ok=False)
    def test_additive_update_and_backup(self):
        self.cli('--only','25')
        out=self.cli('--only','26','--update')
        self.assertIn('omics-ot',out['skills']);self.assertTrue(Path(out['backup']).is_dir())
        self.assertEqual(self.cli('--check')['skills'],3)
    def test_unknown_name(self):self.cli('--only','../../escape',ok=False)
    def test_unknown_profile(self):self.cli('--profile','all-invalid',ok=False)
    def test_project_scope(self):
        p=self.base/'project';p.mkdir()
        out=self.cli('--scope','project','--project',str(p),'--profile','router',dest=False)
        self.assertEqual(Path(out['destination']),p/'.agents/skills')
    def test_project_required(self):self.cli('--scope','project',dest=False,ok=False)
    def test_conflicting_flags(self):self.cli('--scope','project','--project',str(self.base),ok=False)
    def test_foreign_collision_preserved(self):
        p=self.dest/'omics-research';p.mkdir(parents=True);(p/'SKILL.md').write_text('user file')
        self.cli(ok=False);self.assertEqual((p/'SKILL.md').read_text(),'user file')
    def test_unrelated_skill_preserved(self):
        p=self.dest/'nature-reader';p.mkdir(parents=True);(p/'SKILL.md').write_text('unchanged')
        self.cli();self.assertEqual((p/'SKILL.md').read_text(),'unchanged')
    @unittest.skipUnless(hasattr(Path,'symlink_to'),'symlinks unavailable')
    def test_symlink_destination_rejected(self):
        p=self.base/'real';p.mkdir();self.dest.parent.mkdir(parents=True);self.dest.symlink_to(p,target_is_directory=True)
        self.cli(ok=False);self.assertEqual(list(p.iterdir()),[])
    def test_edited_file_detected_and_preserved(self):
        self.cli('--profile','router');p=self.dest/'omics-research/SKILL.md';p.write_text(p.read_text()+'\nUSER EDIT\n')
        self.cli('--check',ok=False);self.cli('--update',ok=False);self.assertIn('USER EDIT',p.read_text())
    def test_missing_dependency_detected(self):
        self.dest.mkdir(parents=True);shutil.copytree(ROOT/'skills/omics-ot',self.dest/'omics-ot')
        with self.assertRaises(ValueError):check_tree(self.dest)
    def test_unsafe_manifest_rejected(self):
        state=self.dest.parent/'omics-method-research-github'
        write_json(state/'install-manifest.json',{'owner':OWNER,'skills':{'../escape':{}}})
        self.cli('--update',ok=False)
    def test_concurrent_install_lock_rejected(self):
        (self.dest.parent/'omics-method-research-github/.install-lock').mkdir(parents=True)
        self.cli(ok=False);self.assertFalse(self.dest.exists())
    def test_legacy_migration_keeps_library(self):
        p=self.dest/'omics-research';p.mkdir(parents=True);(p/'SKILL.md').write_text('legacy wrapper')
        legacy=self.dest.parent/'omics-method-research';(legacy/'library').mkdir(parents=True)
        (legacy/'library/KEEP').write_text('do not delete')
        write_json(legacy/'install-manifest.json',{'owner':'omics-method-research-codex-adapter',
                    'skills':{'omics-research':{'files':inventory(p)}}})
        out=self.cli('--migrate-v02','--profile','router')
        self.assertTrue(out['legacy_library_preserved']);self.assertTrue((legacy/'library/KEEP').exists())
        self.assertTrue((Path(out['backup'])/'skills/omics-research/SKILL.md').exists())
    def test_legacy_edited_rejected(self):
        p=self.dest/'omics-research';p.mkdir(parents=True);(p/'SKILL.md').write_text('old')
        state=self.dest.parent/'omics-method-research'
        write_json(state/'install-manifest.json',{'owner':'omics-method-research-codex-adapter',
                   'skills':{'omics-research':{'files':inventory(p)}}})
        (p/'SKILL.md').write_text('local edit')
        self.cli('--migrate-v02',ok=False);self.assertEqual((p/'SKILL.md').read_text(),'local edit')
    def test_rollback_after_postcheck_failure(self):
        args=argparse.Namespace(dest=str(self.dest),project=None,scope='user',list=False,check=False,
           profile='router',only=None,migrate_v02=False,update=False,dry_run=False)
        real=install_codex.check_tree;count=[0]
        def check(*a,**kw):
            count[0]+=1
            if count[0]==2:raise ValueError('injected post-install failure')
            return real(*a,**kw)
        with patch.object(install_codex,'check_tree',side_effect=check):
            with self.assertRaises(ValueError):install_codex.run(args)
        self.assertFalse((self.dest/'omics-research').exists())
        self.assertFalse((self.dest.parent/'omics-method-research-github/install-manifest.json').exists())
    def test_stateless_check_after_copy(self):
        shutil.copytree(ROOT/'skills',self.dest)
        p=subprocess.run([sys.executable,str(ROOT/'scripts/check_installed.py'),'--dest',str(self.dest)],text=True,capture_output=True)
        self.assertEqual(p.returncode,0,p.stderr)
    def test_publish_plan_no_side_effects(self):
        out=plan('example-owner/omics-method-research-skills','private',True)
        self.assertFalse(out['writes_performed']);self.assertTrue(out['create_only'])
        self.assertNotIn('--force',str(out));self.assertTrue(out['upload_zip_as_draft_release'])
    def test_publish_requires_valid_repo(self):
        for repo in ['https://github.com/x/y','../x','-x/y','token@github.com/x/y']:
            with self.assertRaises(ValueError):plan(repo,'private')
    def test_archive_reproducible(self):
        a=build(self.base/'a.zip');b=build(self.base/'b.zip');self.assertEqual(a['sha256'],b['sha256'])
    @unittest.skipUnless(shutil.which('git'),'git unavailable')
    def test_fresh_local_git_clone_install(self):
        origin=self.base/'origin';origin.mkdir()
        allow=json.loads((ROOT/'RELEASE_FILES.json').read_text())['files']+['RELEASE_FILES.json']
        for rel in allow:
            p=origin/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/rel,p)
        def git(*args,cwd=origin):
            subprocess.run(['git',*args],cwd=cwd,check=True,capture_output=True,timeout=30)
        git('init','-b','main');git('add','.')
        git('-c','user.name=DeploymentTest','-c','user.email=deployment@example.invalid','commit','-m','Local packaging fixture')
        clone=self.base/'clone';git('clone','--no-hardlinks',str(origin),str(clone))
        out=subprocess.run([sys.executable,str(clone/'install_codex.py'),'--dest',str(self.dest)],capture_output=True,text=True,timeout=30)
        self.assertEqual(out.returncode,0,out.stderr);self.assertEqual(check_tree(self.dest)['skills'],29)

if __name__=='__main__':unittest.main()
