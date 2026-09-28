# Deployment references

Consulted 2026-09-28. These are upstream primary sources, not vendored code.
Commands and schemas can change; consult the actual installed version before use.

1. OpenAI, Build skills — local skill directories, SKILL.md metadata, skill-installer and plugin distribution.
   https://developers.openai.com/codex/skills (redirects to https://learn.chatgpt.com/docs/build-skills)
2. OpenAI, Package your plugin — portable and compatibility manifests, local marketplaces.
   https://developers.openai.com/plugins/build/plugins
3. OpenAI skills catalog and system installer — GitHub directory installation and explicit --dest/--path.
   https://github.com/openai/skills
   https://github.com/openai/skills/tree/main/skills/.system/skill-installer
   The catalog currently marks itself deprecated in favor of plugin examples; local skill installation remains described.
4. Nature-skills — independent skill folders and explicit shared support during selective installation.
   https://github.com/Yuan1z0825/nature-skills
5. Vercel skills CLI — add/list, GitHub/local sources, --skill, --agent, --global and --copy.
   https://github.com/vercel-labs/skills
   https://github.com/vercel-labs/skills/blob/main/src/skills.ts
   https://github.com/vercel-labs/skills/blob/main/package.json
   Source observed at version 1.5.22; Node engines >=22.20.0. Mutable main is not a pinned release audit.
6. GitHub CLI, repo create — explicit visibility, --source and --push.
   https://cli.github.com/manual/gh_repo_create
7. GitHub CLI, release create — assets, draft release, --verify-tag.
   https://cli.github.com/manual/gh_release_create

No claim of official affiliation, endorsement, or full upstream client compatibility testing.
