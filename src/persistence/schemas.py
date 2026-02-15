from pydantic import BaseModel


class ProgressRecord(BaseModel):
    last_action: str
    output: str
