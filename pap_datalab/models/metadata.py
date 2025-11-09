from pydantic import BaseModel, AwareDatetime
import typing

class DepdevPsgcPublications(BaseModel):
    name: str
    column_mappings: typing.Dict[str, str]
    valid_from: AwareDatetime
    sheet_name: str
