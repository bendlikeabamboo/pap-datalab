create table if not exists psgc.fact_population_by_administrative_area
(
    surrogate_id UUID default generateUUIDv4(),
    ingestion_datetime DateTime ('Asia/Manila') default now('Asia/Manila'),
    psgc_id String,
    population UInt32,
    valid_from DateTime ('Asia/Manila')
)
engine = MergeTree()
order by psgc_id
