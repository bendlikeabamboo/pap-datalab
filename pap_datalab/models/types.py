from enum import Enum

from clickhouse_sqlalchemy import types

asia_timezone = types.DateTime()

SettlementTypeEnum = Enum(
    "SettlementTypeEnumORM",
    [
        ("urban", 1),
        ("rural", 2),
        ("-", 3),
    ],
)


BarangayStatusEnum = Enum(
    "BarangayStatusEnumORM",
    [
        ("poblacion", 1),
        ("capital", 2),
    ],
)
