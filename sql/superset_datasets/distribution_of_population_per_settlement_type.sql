select
    psgc_dae.psgc_id as barangay_psgc_id,
    psgc_dae.region_mapper as region_psgc_id,
    psgc_dae.province_or_highly_urbanized_city_mapper
        as province_or_city_psgc_id,
    psgc_dae.municipality_or_city_mapper as municipality_or_city_psgc_id,
    psgc_dae.settlement_type as psgc_settlement_type,
    reg.psgc_name as region,
    prov.psgc_name as province_or_city,
    mun.psgc_name as municipality_or_city,
    sum(psgc_fpbaa.population) as population
from psgc.dim_administrative_area as psgc_dae
left join
    psgc.fact_population_by_administrative_area as psgc_fpbaa
    on psgc_dae.psgc_id = psgc_fpbaa.psgc_id
left join
    psgc.dim_administrative_area as reg
    on psgc_dae.region_mapper = reg.psgc_id
left join
    psgc.dim_administrative_area as prov
    on psgc_dae.province_or_highly_urbanized_city_mapper = prov.psgc_id
left join
    psgc.dim_administrative_area as mun
    on psgc_dae.municipality_or_city_mapper = mun.psgc_id

where psgc_dae.geographic_level = 'barangay'
group by
    psgc_dae.settlement_type,
    psgc_dae.region_mapper,
    psgc_dae.province_or_highly_urbanized_city_mapper,
    psgc_dae.municipality_or_city_mapper,
    reg.psgc_name,
    prov.psgc_name,
    mun.psgc_name,
    psgc_dae.psgc_id
