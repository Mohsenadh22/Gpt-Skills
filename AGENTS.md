# Web development skills

This repository contains the web skills requested by its owner. Skills are
vendored in `.agents/skills/`, which allows Codex to discover them when working
in this checkout. `sources.lock.json` records their exact upstream commits and
file hashes.

## Use skills when relevant

For website and web application work, read the relevant `SKILL.md` before
implementation or review. Use the smallest useful set and announce its purpose.

| Task | Skill folder |
| --- | --- |
| Design a page, landing page, dashboard, or component | `frontend-design` |
| Write or optimize React / Next.js | `react-best-practices` |
| Design reusable React components | `composition-patterns` |
| Review UX, accessibility, forms, and interface quality | `web-design-guidelines` |
| Inspect real browser flows | `playwright` |
| Test a local web application | `webapp-testing` |
| Review secure coding | `security-best-practices` |
| Audit SEO | `seo-audit` |
| Implement a supplied Figma design in code | `figma-implement-design` |
| Model application security threats | `security-threat-model` |
| Diagnose GitHub Actions failures | `gh-fix-ci` |
| Address pull request review comments | `gh-address-comments` |
| Investigate existing Sentry events | `sentry` |
| Build ASP.NET Core applications | `aspnet-core` |
| Publish to the selected provider | One of `vercel-deploy`, `cloudflare-deploy`, `netlify-deploy`, `render-deploy` |

Follow the user's chosen framework and hosting provider. Use the deployment
skill only when publishing is requested. For integrations, check that the
required tools and account access are available; a skill does not itself connect
Figma, Sentry, GitHub, or a hosting account.

Adapt shell syntax to the current platform. Some upstream helpers use Bash;
on Windows, use an available Bash runtime or a supported equivalent. Current
system/developer instructions and actual tool documentation take precedence
over upstream examples. Do not claim unsupported commands were executed.

## Maintaining this collection

Preserve upstream skill files and their licenses. Add local behavior to this
file or project documentation rather than silently rewriting upstream files.
When importing an update, record its commit and refresh the manifest hashes.
Run `python scripts/verify_collection.py` before publishing changes.

Install the collection with `python scripts/install_local.py`. Existing local
skills with different contents are preserved; resolve differences explicitly.
