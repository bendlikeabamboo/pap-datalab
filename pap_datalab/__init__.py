"""
Punan and Patlang Datalab
"""

from typing import Dict
from sqlalchemy import MetaData
from sqlalchemy.orm import registry

SCHEMAS = {
    "depdev",
    "deped",
}

schema_registries: Dict[str, registry] = {}

for schema in SCHEMAS:
    metadata = MetaData(schema=schema)
    schema_registries[schema] = registry(metadata=metadata)
