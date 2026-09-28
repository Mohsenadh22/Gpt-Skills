# Third-party sources and licenses

This collection vendors 18 upstream skills without modifying their source
files. The exact commit, source URL, path, and SHA-256 hashes are recorded per
skill in `sources.lock.json`. Local documentation and installer utilities do not
replace the licenses governing upstream content.

| Upstream repository | Selected skills | License information |
| --- | --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | `frontend-design`, `webapp-testing` | Apache-2.0; each skill includes its original `LICENSE.txt` |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `react-best-practices`, `web-design-guidelines`, `composition-patterns` | MIT, as declared in the upstream README; relevant skill frontmatter is preserved |
| [openai/skills](https://github.com/openai/skills) | The 12 selected curated skills | Apache-2.0; each skill includes its original `LICENSE.txt` |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `seo-audit` | MIT; Copyright (c) 2025 Corey Haines; complete license in `licenses/coreyhaines31--marketingskills-LICENSE` |

Vercel's selected snapshot has no standalone root LICENSE file. Its complete
upstream README is preserved in `licenses/vercel-labs--agent-skills-README.md`,
including the MIT license declaration. All original embedded notices and
attributions in vendored files are retained.

Service names and logos included in upstream asset folders remain attributed to
their respective owners. Importing these skills does not grant access to those
services or change their account terms.
