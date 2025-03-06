from pydantic import BaseModel, Field
from typing import List, Optional

class DTEItem(BaseModel):
    NroLinDet: int
    NmbItem: str
    QtyItem: int
    PrcItem: float
    MontoItem: float

class DTEPayload(BaseModel):
    TipoDTE: int = Field(..., description="Tipo de Documento Tributario Electrónico (Ej: 33 para factura afectada)")
    Folio: Optional[int] = Field(0, description="Número de folio (0 si es generado automáticamente)")
    Emisor: str
    Receptor: str
    Items: List[DTEItem]

class DTEResponse(BaseModel):
    code: str
    message: str
    DocumentoDTE: dict
