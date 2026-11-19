# 📖 Spellbook

A unified reference notebook — saved links, code snippets, school notes, and everything worth remembering.

**Live site:** [atamburino.github.io/spellbook](https://atamburino.github.io/spellbook)

## How it works

- A doc bot watches for things to save and opens PRs with structured markdown
- When merged to `main`, GitHub Actions builds and deploys to GitHub Pages
- Everything is markdown (MDX). Everything is searchable. Everything is in one place

## Structure

```
notebook/
├── docs/
│   ├── index.mdx              ← Landing page
│   ├── references/             ← Saved articles, tweets, code patterns
│   │   ├── lua/
│   │   ├── react/
│   │   └── ...
│   └── school/                 ← Master's program notes
├── src/
│   ├── components/
│   │   └── Artifact/           ← Embed interactive HTML/JS in any page
│   └── css/custom.css
└── docusaurus.config.ts
```

## For the doc bot

See [BOT_INSTRUCTIONS.md](BOT_INSTRUCTIONS.md) for the PR format, file template, and contribution rules.

## Local development

```bash
cd notebook
npm install
npm start        # Dev server at localhost:3000
npm run build    # Production build
```

## Other contents

- [School/Computer-Science](School/Computer-Science/Home.md) — class notes (original format)
- `newweek.py` / `newweek.cmd` — weekly workspace generators
