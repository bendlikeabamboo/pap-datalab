import datetime as dt

from clickhouse_sqlalchemy import engines, types
from sqlalchemy import Column

from pap_datalab import schema_registries
from pap_datalab.models.types import (
    BarangayStatusEnum,
    SettlementTypeEnum,
    IncomeClassificationCleanEnum,
    IncomeClassificationEnum,
    CityClassEnum,
    asia_timezone,
)

depdev_registry = schema_registries["depdev"]


@depdev_registry.mapped
class FactBarangay:
    __tablename__ = "fact_population_barangay"
    surrogate_id = Column(types.String, primary_key=True)
    ingestion_datetime = Column(
        asia_timezone, default=lambda: dt.datetime.now(dt.timezone.utc)
    )
    psgc_id = Column(types.String)
    psgc_name = Column(types.String)
    population = Column(types.UInt64)
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)


@depdev_registry.mapped
class DimBarangay:
    __tablename__ = "dim_barangay"
    surrogate_id = Column(types.String, primary_key=True)
    ingestion_datetime = Column(
        asia_timezone, default=lambda: dt.datetime.now(dt.timezone.utc)
    )
    psgc_id = Column(types.String)
    psgc_name = Column(types.String)
    correspondence_code = Column(types.String)
    old_name = Column(types.String)
    settlement_type = Column(types.Nullable(types.Enum8(SettlementTypeEnum)))
    remarks = Column(types.String)
    status = Column(types.Nullable(types.Enum8(BarangayStatusEnum)))
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)


@depdev_registry.mapped
class FactMunicipality:
    __tablename__ = "fact_population_municipality"
    surrogate_id = Column(types.String, primary_key=True)
    ingestion_datetime = Column(
        asia_timezone, default=lambda: dt.datetime.now(dt.timezone.utc)
    )
    psgc_id = Column(types.String)
    psgc_name = Column(types.String)
    population = Column(types.UInt64)
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)


@depdev_registry.mapped
class DimMunicipality:
    __tablename__ = "dim_municipality"
    surrogate_id = Column(types.String, primary_key=True)
    ingestion_datetime = Column(
        asia_timezone, default=lambda: dt.datetime.now(dt.timezone.utc)
    )
    psgc_id = Column(types.String)
    psgc_name = Column(types.String)
    correspondence_code = Column(types.String)
    old_name = Column(types.String)
    income_classification = Column(
        types.Nullable(types.Enum8(IncomeClassificationEnum))
    )
    remarks = Column(types.String)
    status = Column(types.Nullable(types.Enum8(BarangayStatusEnum)))
    income_classification_clean = Column(
        types.Nullable(types.Enum8(IncomeClassificationCleanEnum))
    )
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)


@depdev_registry.mapped
class FactSubmunicipality:
    __tablename__ = "fact_population_submunicipality"
    surrogate_id = Column(types.String, primary_key=True)
    ingestion_datetime = Column(
        asia_timezone, default=lambda: dt.datetime.now(dt.timezone.utc)
    )
    psgc_id = Column(types.String)
    psgc_name = Column(types.String)
    population = Column(types.UInt64)
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)


@depdev_registry.mapped
class DimSubmunicipality:
    __tablename__ = "dim_submunicipality"
    surrogate_id = Column(types.String, primary_key=True)
    ingestion_datetime = Column(
        asia_timezone, default=lambda: dt.datetime.now(dt.timezone.utc)
    )
    psgc_id = Column(types.String)
    psgc_name = Column(types.String)
    correspondence_code = Column(types.String)
    old_name = Column(types.String)
    remarks = Column(types.String)
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)


@depdev_registry.mapped
class FactCity:
    __tablename__ = "fact_population_city"
    surrogate_id = Column(types.String, primary_key=True)
    ingestion_datetime = Column(
        asia_timezone, default=lambda: dt.datetime.now(dt.timezone.utc)
    )
    psgc_id = Column(types.String)
    psgc_name = Column(types.String)
    population = Column(types.UInt64)
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)


@depdev_registry.mapped
class DimCity:
    __tablename__ = "dim_city"
    surrogate_id = Column(types.String, primary_key=True)
    ingestion_datetime = Column(
        asia_timezone, default=lambda: dt.datetime.now(dt.timezone.utc)
    )
    psgc_id = Column(types.String)
    psgc_name = Column(types.String)
    correspondence_code = Column(types.String)
    old_name = Column(types.String)
    city_class = Column(types.Nullable(types.Enum8(CityClassEnum)))
    income_classification = Column(
        types.Nullable(types.Enum8(IncomeClassificationEnum))
    )
    remarks = Column(types.String)
    status = Column(types.Nullable(types.Enum8(BarangayStatusEnum)))
    income_classification_clean = Column(
        types.Nullable(types.Enum8(IncomeClassificationCleanEnum))
    )
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)


@depdev_registry.mapped
class FactProvince:
    __tablename__ = "fact_population_province"
    surrogate_id = Column(types.String, primary_key=True)
    ingestion_datetime = Column(
        asia_timezone, default=lambda: dt.datetime.now(dt.timezone.utc)
    )
    psgc_id = Column(types.String)
    psgc_name = Column(types.String)
    population = Column(types.UInt64)
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)


@depdev_registry.mapped
class DimProvince:
    __tablename__ = "dim_province"
    surrogate_id = Column(types.String, primary_key=True)
    ingestion_datetime = Column(
        asia_timezone, default=lambda: dt.datetime.now(dt.timezone.utc)
    )
    psgc_id = Column(types.String)
    psgc_name = Column(types.String)
    correspondence_code = Column(types.String)
    old_name = Column(types.String)
    income_classification = Column(
        types.Nullable(types.Enum8(IncomeClassificationEnum))
    )
    remarks = Column(types.String)
    income_classification_clean = Column(
        types.Nullable(types.Enum8(IncomeClassificationCleanEnum))
    )
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)


@depdev_registry.mapped
class FactRegion:
    __tablename__ = "fact_population_region"
    surrogate_id = Column(types.String, primary_key=True)
    ingestion_datetime = Column(
        asia_timezone, default=lambda: dt.datetime.now(dt.timezone.utc)
    )
    psgc_id = Column(types.String)
    psgc_name = Column(types.String)
    population = Column(types.UInt64)
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)


@depdev_registry.mapped
class DimRegion:
    __tablename__ = "dim_region"
    surrogate_id = Column(types.String, primary_key=True)
    ingestion_datetime = Column(
        asia_timezone, default=lambda: dt.datetime.now(dt.timezone.utc)
    )
    psgc_id = Column(types.String)
    psgc_name = Column(types.String)
    correspondence_code = Column(types.String)
    old_name = Column(types.String)
    remarks = Column(types.String)
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)

    ##