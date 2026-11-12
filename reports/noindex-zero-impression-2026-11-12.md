# Zero-impression guide noindex snapshot (2026-11-12)

Source property: `sc-domain:microswitchguide.com`.

- Search Console's 16-month Web performance report showed 51 clicks and 5,647 impressions, with visible activity from 2026-10-11 through 2026-11-10. The site's guides were published from 2026-10-13.
- The BigQuery bulk export in `project-b3451fdf-e27e-4cdf-af6.searchconsole` covers 2026-10-12 through 2026-11-09. Its `searchdata_url_impression` table showed 1,382 distinct guide URLs with Web impressions. The corresponding `ExportLog` has both daily namespaces through 2026-11-09.
- The Search Console 7-day page report, which includes 2026-11-10, added two guide URLs not in the BigQuery history: `/guides/diy-micro-switch/` and `/guides/air-compressor-home-position-micro-switch-wiring/`.
- The current public sitemap and repository each contain the same 5,631 guide URLs. The 1,382 BigQuery URLs plus those two Search Console URLs remain indexable. `_data/noindex_paths.json` lists the other 4,247 guides.

The manifest is a fixed snapshot. Newly published posts remain indexable unless explicitly added. The noindex meta tag leaves each page accessible for users and crawlers; the sitemap excludes its URL. Google removes an already indexed URL after recrawling it, so deployment is not proof that Search results have updated.
