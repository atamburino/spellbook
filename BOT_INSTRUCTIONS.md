# Doc Bot — Spellbook Contribution Guide

When saving a reference to the Spellbook, create a PR that adds **one `.mdx` file** to the correct subfolder under `notebook/docs/references/`.

## File structure

```
notebook/docs/references/
├── _category_.json          ← already exists, don't modify
├── artifact-demo.mdx        ← example with interactive HTML
├── lua/
│   ├── _category_.json      ← one per topic folder
│   └── lua-sdks-for-rex.mdx
├── react/
│   ├── _category_.json
│   └── some-react-pattern.mdx
└── devops/
    ├── _category_.json
    └── cool-ci-trick.mdx
```

## Creating a new topic folder

If the reference doesn't fit an existing folder, create a new one:

1. Create `notebook/docs/references/<topic>/` (lowercase, kebab-case)
2. Add a `_category_.json`:

```json
{
  "label": "<Topic Name>",
  "position": 10,
  "collapsed": false
}
```

3. Add the `.mdx` file inside it.

## MDX file template

Every saved reference must use this exact frontmatter + body structure:

```mdx
---
title: "<Descriptive title of what was saved>"
sidebar_label: <Short label for the sidebar>
tags: [tag1, tag2, tag3]
date: YYYY-MM-DD
custom_edit_url: null
---

# <Same title as frontmatter>

> **Source:** [Author Name (@handle)](https://original-url) · <Date>
>
> **Saved via:** <How it was requested — X reply, DM, etc.>

## The idea

<1-3 sentence plain-English summary of what this is about>

## Code / Content

<The actual content — code blocks, explanations, screenshots>

## Key takeaways

- <Bullet points of what's worth remembering>
- <Patterns, tricks, or insights>
```

## Rules

1. **File naming:** `kebab-case-short-name.mdx` — no dates in the filename
2. **Tags:** lowercase, comma-separated, 3-6 tags that describe the technology and concept
3. **Code blocks:** Always include the language identifier (```lua, ```python, etc.)
4. **Source attribution:** Always link to the original URL
5. **One file per reference** — don't batch multiple saves into one file
6. **MDX format required** — use `.mdx` extension, not `.md` (enables interactive components)
7. **No changes to other files** — the sidebar auto-generates from the folder structure. Don't edit `sidebars.ts`, `docusaurus.config.ts`, or any `_category_.json` unless creating a new topic folder

## Adding interactive artifacts (optional)

If the reference benefits from an interactive demo, add this at the top of the MDX body:

```mdx
import Artifact from '@site/src/components/Artifact';
```

Then embed the HTML:

```mdx
<Artifact
  title="Demo name"
  height={300}
  html={`
    <html>
    <body>
      <!-- interactive HTML/CSS/JS here -->
    </body>
    </html>
  `}
/>
```

## Large interactive charts

Large interactive charts (like Flux flowcharts) do not go inline with `<Artifact>`. The Artifact iframe is sandboxed (`allow-scripts` only, so citation links cannot open a new tab) and fixed-height. Put the standalone HTML, with its source JSON beside it, in `notebook/static/flux/`, and link the HTML from the reference `.mdx`:

```mdx
[Open the chart](pathname:///flux/your-chart.html)
```

`pathname://` serves the file as its own page and still picks up the site `baseUrl`.

## PR format

- **Branch:** `doc/<kebab-case-topic>`
- **Title:** `doc: save <short-description>`
- **Body:** One-liner about what was saved and why

## Example PR

Branch: `doc/lua-sdks-for-rex`
Title: `doc: save lua-sdks-for-rex`
Files changed:
- `notebook/docs/references/lua/lua-sdks-for-rex.mdx` (added)
