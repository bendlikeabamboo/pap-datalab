from enum import Enum

from clickhouse_sqlalchemy import types

asia_timezone = types.DateTime()
asia_timezone.timezone = "Asia/Manila"

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

IncomeClassificationEnum = Enum(
    "IncomeClassificationEnumORM",
    [
        ("1st", 1),   
        ("1st*", 2),
        ("2nd", 3),
        ("2nd*", 4),
        ("3rd", 5),
        ("3rd*", 6),
        ("4th", 7),
        ("4th*", 8),
        ("5th", 9),
        ("5th*", 10),
        ("-", 11),
    ],
)

IncomeClassificationCleanEnum = Enum(
    "IncomeClassificationEnumORM",
    [
        ("1st", 1),
        ("2nd", 2),
        ("3rd", 3),
        ("4th", 4),
        ("5th", 5),
    ],
)

CityClassEnum = Enum(
    "CityClassEnum",
    [
        "highly_urbanized_city",
        "independent_component_city",
        "component_city",
    ],
)
