import datetime as dt

from clickhouse_sqlalchemy import engines, types
from sqlalchemy import Column

from pap_datalab import schema_registries
from pap_datalab.models.types import (
    BarangayStatusEnum,
    SettlementTypeEnum,
    asia_timezone,
)

depdev_registry = schema_registries["depdev"]


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
    status = Column(types.Nullable(types.Enum8(BarangayStatusEnum)))
    remarks = Column(types.String)
    identity_hash = Column(types.String)
    fields_hash = Column(types.String)
    valid_from = Column(asia_timezone)
    valid_to = Column(types.Nullable(asia_timezone))
    engine = engines.MergeTree(order_by=["surrogate_id"])
    __table_args__ = (engines.MergeTree(order_by=["surrogate_id"]),)
