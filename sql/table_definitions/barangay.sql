create table if not exists dim_administrative_area
(
    surrogate_id UUID default generateUUIDv4(),
    ingestion_datetime DateTime ('Asia/Manila') default now('Asia/Manila'),
    psgc_id String,
    psgc_name String,
    geographic_level String,
    settlement_type String,
    income_classification String,
    city_class String,
    psgc_extras String,
    barangay_status String,
    barangay_code String,
    barangay_mapper String,
    municipality_or_city_code String,
    municipality_or_city_mapper String,
    province_or_highly_urbanized_city_code String,
    province_or_highly_urbanized_city_mapper String,
    region_code String,
    region_mapper String,
    legacy_psgc_id String,
    legacy_psgc_name String,
    valid_from DateTime ('Asia/Manila')
)
engine = MergeTree()
order by psgc_id
