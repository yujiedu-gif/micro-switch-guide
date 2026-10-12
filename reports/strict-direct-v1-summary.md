# Strict direct topic cleanup

Classifier: `strict-direct-v1`

## Keyword decisions

- Total raw keywords preserved: 15,458
- Accepted for production: 444
- Held for brand, model, or commercial review: 374
- Rejected as non-direct or explicit drift: 14,640

Only approved direct component-family terms qualify. DataForSEO intent remains
stored as evidence but cannot override the deterministic text gate.

## Existing published articles

- Published before cleanup: 294
- Retained with direct scope and complete source coverage: 18
- Quarantined model articles: 8
- Retracted non-direct articles: 234
- Temporarily withdrawn for uncovered source-pack terms: 34

The retained set has four valid internal links per article and no links to a
withdrawn page.

## Vector index

- Qdrant collection: `msg_topics_strict_v1`
- Accepted keyword vectors: 444
- Topic clusters: 255
- Borderline similarity pairs held for review: 979

## Verification

- Selected keywords outside `accept`: 0
- Active jobs outside `accept`: 0
- Published articles with uncovered center-topic facts: 0
- Broken internal links: 0
- Published articles passing schema, editorial, and source-pack validation: 18/18
- Unit tests: 52 passed
- Jekyll production build: passed
