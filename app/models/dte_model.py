from pydantic import BaseModel
from typing import List, Dict

class DteItem(BaseModel):
    NroLinDet: int
    CdgItem: Dict[str, str]
    NmbItem: str
    DscItem: str
    QtyItem: str
    UnmdItem: str
    PrcItem: str
    MontoItem: str

class DteRequest(BaseModel):
    DteSend: Dict[str, List[Dict]]
