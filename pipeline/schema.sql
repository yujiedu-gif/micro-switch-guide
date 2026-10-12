PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

CREATE TABLE IF NOT EXISTS runs (
  run_id TEXT PRIMARY KEY,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  stage TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('running','complete','failed','paused')),
  config_hash TEXT NOT NULL,
  skill_hash TEXT NOT NULL,
  metadata_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS api_costs (
  cost_id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id TEXT NOT NULL REFERENCES runs(run_id),
  provider TEXT NOT NULL,
  operation TEXT NOT NULL,
  request_id TEXT,
  amount_usd REAL NOT NULL CHECK (amount_usd >= 0),
  units INTEGER,
  recorded_at TEXT NOT NULL,
  metadata_json TEXT NOT NULL DEFAULT '{}',
  UNIQUE(provider, request_id)
);

CREATE TABLE IF NOT EXISTS keywords (
  keyword_id TEXT PRIMARY KEY,
  keyword TEXT NOT NULL,
  normalized_keyword TEXT NOT NULL UNIQUE,
  source_endpoint TEXT,
  location_code INTEGER NOT NULL,
  language_code TEXT NOT NULL,
  search_volume INTEGER,
  cpc REAL,
  competition TEXT,
  intent TEXT,
  exclusion_reason TEXT,
  serp_signature_json TEXT NOT NULL DEFAULT '[]',
  data_version TEXT,
  trend_json TEXT NOT NULL DEFAULT '{}',
  cluster_id TEXT,
  selected INTEGER NOT NULL DEFAULT 0 CHECK (selected IN (0,1)),
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS keyword_scope_decisions (
  keyword_id TEXT NOT NULL REFERENCES keywords(keyword_id),
  classifier_version TEXT NOT NULL,
  decision TEXT NOT NULL CHECK(decision IN ('accept','hold','reject')),
  scope_class TEXT NOT NULL,
  reason_codes_json TEXT NOT NULL DEFAULT '[]',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  PRIMARY KEY(keyword_id, classifier_version)
);

CREATE TABLE IF NOT EXISTS technical_relationships (
  relationship_id TEXT PRIMARY KEY,
  ontology_version TEXT NOT NULL,
  entity TEXT NOT NULL,
  component TEXT,
  relation TEXT NOT NULL,
  function TEXT NOT NULL,
  confidence TEXT NOT NULL CHECK(confidence IN ('candidate','confirmed','rejected')),
  evidence_mode TEXT NOT NULL CHECK(evidence_mode IN ('discovery_only','publishable','mixed')),
  discovery_source_ids_json TEXT NOT NULL DEFAULT '[]',
  publishable_claim_ids_json TEXT NOT NULL DEFAULT '[]',
  allowed_tasks_json TEXT NOT NULL DEFAULT '[]',
  blocked_tasks_json TEXT NOT NULL DEFAULT '[]',
  conditional_language_required INTEGER NOT NULL DEFAULT 1 CHECK(conditional_language_required IN (0,1)),
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  UNIQUE(ontology_version,entity,component,relation,function)
);

CREATE TABLE IF NOT EXISTS keyword_derivations (
  keyword_id TEXT NOT NULL REFERENCES keywords(keyword_id),
  generator_version TEXT NOT NULL,
  relation_version TEXT NOT NULL,
  origin_keyword_ids_json TEXT NOT NULL DEFAULT '[]',
  entity TEXT,
  component TEXT,
  function TEXT,
  reader_task TEXT NOT NULL,
  answer_type TEXT NOT NULL,
  relation_type TEXT NOT NULL,
  template_id TEXT NOT NULL,
  risk_level TEXT NOT NULL,
  content_signature TEXT NOT NULL,
  validation_status TEXT NOT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  PRIMARY KEY(keyword_id,generator_version)
);

CREATE TABLE IF NOT EXISTS embeddings (
  object_type TEXT NOT NULL,
  object_id TEXT NOT NULL,
  model TEXT NOT NULL,
  dimensions INTEGER NOT NULL,
  vector_sha256 TEXT NOT NULL,
  qdrant_point_id TEXT,
  created_at TEXT NOT NULL,
  PRIMARY KEY(object_type, object_id, model)
);

CREATE TABLE IF NOT EXISTS clusters (
  cluster_id TEXT PRIMARY KEY,
  algorithm_version TEXT NOT NULL,
  threshold REAL NOT NULL,
  primary_keyword_id TEXT REFERENCES keywords(keyword_id),
  label TEXT,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS content_jobs (
  job_id TEXT PRIMARY KEY,
  created_run_id TEXT REFERENCES runs(run_id),
  keyword_id TEXT NOT NULL REFERENCES keywords(keyword_id),
  custom_id TEXT NOT NULL UNIQUE,
  parent_custom_id TEXT,
  status TEXT NOT NULL,
  plan_batch_id TEXT,
  article_batch_id TEXT,
  title TEXT,
  slug TEXT UNIQUE,
  category TEXT,
  owned_question TEXT,
  plan_json TEXT,
  article_json TEXT,
  retry_count INTEGER NOT NULL DEFAULT 0,
  validation_json TEXT,
  source_pack_json TEXT,
  duplicate_of_job_id TEXT REFERENCES content_jobs(job_id),
  text_fingerprint TEXT,
  semantic_score REAL,
  git_commit TEXT,
  published_url TEXT,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sources (
  source_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  publisher TEXT NOT NULL,
  url TEXT NOT NULL UNIQUE,
  source_type TEXT NOT NULL,
  document_version TEXT,
  document_date TEXT,
  page_or_section TEXT,
  retrieved_at TEXT NOT NULL,
  content_hash TEXT NOT NULL,
  editorial_block_names_json TEXT NOT NULL DEFAULT '[]',
  evidence_summary TEXT
);

CREATE TABLE IF NOT EXISTS claims (
  claim_id TEXT PRIMARY KEY,
  subject TEXT NOT NULL,
  predicate TEXT NOT NULL,
  value_json TEXT NOT NULL,
  unit TEXT,
  conditions_json TEXT NOT NULL DEFAULT '{}',
  scope TEXT NOT NULL,
  confidence TEXT NOT NULL,
  status TEXT NOT NULL,
  conflicts_with_json TEXT NOT NULL DEFAULT '[]',
  supersedes_json TEXT NOT NULL DEFAULT '[]',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS claim_sources (
  claim_id TEXT NOT NULL REFERENCES claims(claim_id),
  source_id TEXT NOT NULL REFERENCES sources(source_id),
  PRIMARY KEY(claim_id, source_id)
);

CREATE TABLE IF NOT EXISTS article_claims (
  job_id TEXT NOT NULL REFERENCES content_jobs(job_id),
  claim_id TEXT NOT NULL REFERENCES claims(claim_id),
  usage_status TEXT NOT NULL CHECK (usage_status IN ('used','excluded')),
  PRIMARY KEY(job_id, claim_id)
);

CREATE TABLE IF NOT EXISTS internal_links (
  source_job_id TEXT NOT NULL REFERENCES content_jobs(job_id),
  target_job_id TEXT NOT NULL REFERENCES content_jobs(job_id),
  relation TEXT NOT NULL CHECK (relation IN ('pillar','supporting','related')),
  anchor_text TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('planned','valid','broken','blocked')),
  PRIMARY KEY(source_job_id, target_job_id),
  CHECK(source_job_id <> target_job_id)
);

CREATE TABLE IF NOT EXISTS batch_requests (
  custom_id TEXT PRIMARY KEY,
  run_id TEXT NOT NULL REFERENCES runs(run_id),
  kind TEXT NOT NULL CHECK (kind IN ('plan','article','review','repair')),
  job_id TEXT REFERENCES content_jobs(job_id),
  endpoint TEXT NOT NULL,
  model TEXT NOT NULL,
  input_sha256 TEXT NOT NULL,
  batch_id TEXT,
  input_file_id TEXT,
  output_file_id TEXT,
  error_file_id TEXT,
  parent_custom_id TEXT,
  retry_count INTEGER NOT NULL DEFAULT 0,
  usage_json TEXT NOT NULL DEFAULT '{}',
  status TEXT NOT NULL,
  response_json TEXT,
  error_json TEXT,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS provider_objects (
  provider TEXT NOT NULL,
  object_type TEXT NOT NULL,
  local_id TEXT NOT NULL,
  remote_id TEXT,
  status TEXT NOT NULL,
  payload_sha256 TEXT,
  metadata_json TEXT NOT NULL DEFAULT '{}',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  PRIMARY KEY(provider, object_type, local_id)
);

CREATE TABLE IF NOT EXISTS run_reports (
  run_id TEXT PRIMARY KEY REFERENCES runs(run_id),
  report_json TEXT NOT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS semantic_reviews (
  job_id TEXT PRIMARY KEY REFERENCES content_jobs(job_id),
  custom_id TEXT NOT NULL UNIQUE,
  passed INTEGER NOT NULL CHECK(passed IN (0,1)),
  review_json TEXT NOT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS similarity_reviews (
  object_type TEXT NOT NULL,
  left_id TEXT NOT NULL,
  right_id TEXT NOT NULL,
  cosine_score REAL NOT NULL,
  serp_overlap REAL,
  label TEXT,
  status TEXT NOT NULL CHECK(status IN ('needs_review','labeled','applied')),
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  PRIMARY KEY(object_type,left_id,right_id)
);

CREATE INDEX IF NOT EXISTS idx_keywords_cluster ON keywords(cluster_id);
CREATE INDEX IF NOT EXISTS idx_scope_decision ON keyword_scope_decisions(classifier_version, decision);
CREATE INDEX IF NOT EXISTS idx_relationship_entity ON technical_relationships(ontology_version,entity,component);
CREATE INDEX IF NOT EXISTS idx_derivation_status ON keyword_derivations(generator_version,validation_status);
CREATE UNIQUE INDEX IF NOT EXISTS idx_derivation_signature ON keyword_derivations(generator_version,content_signature);
CREATE INDEX IF NOT EXISTS idx_jobs_status ON content_jobs(status);
CREATE INDEX IF NOT EXISTS idx_batch_status ON batch_requests(status);
CREATE INDEX IF NOT EXISTS idx_costs_run_provider ON api_costs(run_id, provider);
