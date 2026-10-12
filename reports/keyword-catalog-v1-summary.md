# Micro-switch keyword catalog v1

Date: 2026-10-12

## Acceptance result

- Requested keywords: 10,000
- Generated keywords: 10,000
- Normalized unique keywords: 10,000
- Strict direct-topic accepts: 10,000
- Existing-database duplicates: 0
- Paid calls used by catalog generation: 0
- Database mutations: 0
- Articles or plans generated: 0

## Distribution

- Industrial machine applications: 5,184
- Motion and access systems: 1,611
- Specific appliance, vehicle, transport, medical, office, and control applications: 2,205
- Actuator topics: 173
- Mechanical and electrical parameters: 239
- Contact and circuit topics: 222
- Environmental topics: 175
- Failure topics: 191

Every row contains an approved direct micro-switch term and passes the strict topic classifier. Keyboard switches, household lighting wiring, Nintendo, guitar electronics, brand navigation, commercial-intent wording, product models, and normalized duplicates are excluded.

The generated CSV and JSONL are runtime deliverables under `pipeline/state/outputs/keyword-catalog-v1/`. They are keyword candidates only. They do not assert that every application uses the same switch design, and they do not bypass later search-volume, evidence, planning, or article-content checks.

An asynchronous DataForSEO round using 20 direct micro-switch seeds returned 224 rows, of which 31 were net-new. Those rows were imported into the local raw keyword store, but the deterministic catalog excludes all keywords already present in that store, so the delivered 10,000 are net-new relative to the database.
