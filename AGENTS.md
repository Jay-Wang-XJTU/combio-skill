# Repository maintenance rules

This repository distributes research workflows, not biological data.
Read README.md, docs/INSTALL_ZH.md, and provenance/library_transform.json before changing layout.
Only the 29 public skills/*/SKILL.md files are discoverable entries. Inner GUIDE.md files are references.
Keep omics-research/library and all relative links intact. Do not duplicate it into every skill.
Run `python3 scripts/validate_repo.py` and `python3 -m unittest discover -s tests -v` after changes.
Do not run scientific experiments or install dependencies just to load a skill.
Do not publish, alter repository visibility, change licenses, or upload data without explicit authorization.
Historical scientific test outputs are not execution evidence for the current session.
Never store tokens, local auth.json, SSH keys, patient data, or unpublished project results here.
