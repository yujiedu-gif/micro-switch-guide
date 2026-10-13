# Search discovery integrations

## IndexNow

Run `./bin/search-discovery indexnow-key-init` once and commit the root text file. After the file is deployed, verify the returned URL serves exactly the file contents. The main-branch workflow derives changed guide URLs from the Git diff, waits for the GitHub Pages build of that commit and the live key and pages, then submits up to 10,000 URLs per request with an explicit `keyLocation`. For manual recovery use `./bin/search-discovery indexnow-submit --before <previous-deployed-sha>` after the key is live. Submit only URLs added, materially updated, or removed since enabling IndexNow; do not backfill unchanged historical URLs. It accepts only URLs on the configured canonical host. A 200/202 response means the notification was received, not that a page was indexed. Confirm receipt in Bing Webmaster Tools. IndexNow serves participating search engines; Google discovery continues through the Sitemap.

## Search Console to BigQuery

The configured project ID is `fluent-justice-494303-g3`. Google's native bulk export needs billing on that project, **BigQuery API and BigQuery Storage API** enabled (the BigQuery Connection API is a different service), and the Search Console property owner. Grant `search-console-data-export@system.gserviceaccount.com` the project roles **BigQuery Job User** and **BigQuery Data Editor**. In the Search Console property open Settings → Bulk data export and select the project ID, `searchconsole` dataset, and dataset location. Google creates `searchdata_url_impression`, `searchdata_site_impression`, and `ExportLog` at first export, which can take up to 48 hours. It does not backfill older days.

For a read-only local check, configure Google Application Default Credentials with permission to query the dataset and run:

```bash
./bin/search-discovery bigquery-check
./bin/search-discovery bigquery-sync
```

The commands default to the configured project, the `searchconsole` dataset and `US` location. Override `MSG_BIGQUERY_DATASET` and `MSG_BIGQUERY_LOCATION` if different choices were made in Search Console. The query aggregates repeated URL impression rows across the last 90 days and caps billed scan bytes at 1 GB. `bigquery-check` prints a count without changing SQLite; `bigquery-sync` upserts the current URL aggregates into `search_console_url_performance` in the ignored SQLite database. `--show-sql` shows the exact SQL without connecting. This is performance data, not a URL index-status feed; page index status requires Search Console's URL Inspection API. Review the Cloud project's billing and dataset retention before starting continuous export.

Sources: [Search Console setup](https://support.google.com/webmasters/answer/12917675), [BigQuery export tables](https://support.google.com/webmasters/answer/12917991), [Bing IndexNow setup](https://www.bing.com/indexnow/getstarted), [IndexNow protocol](https://www.indexnow.org/documentation).
