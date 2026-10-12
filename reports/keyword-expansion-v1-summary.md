# Keyword expansion v1 validation

Date: 2026-10-12

This run was local and read-only. It did not change keyword production eligibility, submit a provider request, or generate an article.

## Results

- Rejected source keywords inspected: 14,640
- Raw rows matching a bounded relationship pattern: 1,900
- Unique relationship bases after canonicalization: 35
- Unique generated candidates: 212
- Low-risk candidates pending evidence and demand checks: 145
- Evidence-sensitive candidates held: 67
- Planning-ready sample exported: 100
- Unique keywords in the sample: 100
- Unique content signatures in the sample: 100
- Paid API calls: 0

Candidate relationships:

- Direct application: 113
- Direct technical: 91
- Bounded comparison: 8

The audit deliberately collapses wording variants that map to one content identity. For example, dryer door, interlock, and safety-switch wording does not create three function articles when the entity, mechanism, reader task, and answer type are the same.

## Boundaries

- Keyboard, household wiring, distribution switchgear, gaming, guitar, and generic marine/panel drift is rejected before generation.
- Broad automotive topics are rejected; only a named subsystem can form a candidate.
- Testing, continuity, adjustment, selection, rating, wiring, replacement, safety, and compatibility tasks remain held until appropriate evidence exists.
- Application candidates require conditional wording until the relationship is confirmed for the relevant design.
- Commercial and manufacturer technical sources are allowed when claims preserve exact scope. Publisher names may appear in Sources; every rendered external link is `nofollow`. Marketing, ranking, and purchasing language remains prohibited.

## Scale conclusion

The existing 15,458-keyword corpus supplies a valid first wave, but only 35 unique relationship bases under the current bounded ontology. It cannot support 10,000 non-repetitive articles by itself. The sustainable route remains ontology growth plus asynchronous DataForSEO expansion. The next scale gate is to add verified equipment, component, parameter, environment, and failure relationships, then run plan and section-plan semantic deduplication before any article Batch.

Runtime audit files are stored under ignored `pipeline/state/outputs/keyword-expansion-v1/`.
