from pydantic import BaseModel
from typing import Union

class KeyLogData(BaseModel):
    keyboardData: Union[str, None] = None