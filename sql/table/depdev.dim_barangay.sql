-- Target: Clickhouse
create table if not exists depdev.dim_administrative_area
(
    surrogate_id UUID default generateUUIDv4(),
    ingestion_datetime DateTime ('Asia/Manila') default now('Asia/Manila'),
    psgc_id String,
    psgc_name String,
    correspondence_code String,
    old_name String,
    settlement_type Enum8 ("urban","rural"),
    status Enum8 ("", "poblacion","capital"),
    remarks String,
    valid_from DateTime ('Asia/Manila'),
    valid_to DateTime('Asia/Manila')
)
engine = MergeTree()
order by psgc_id
