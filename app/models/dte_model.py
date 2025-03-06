from pydantic import BaseModel
from typing import List, Dict

# Estructura para el encabezado del documento
class IdDoc(BaseModel):
    TipoDTE: str
    Folio: str
    FchEmis: str
    FmaPago: str
    TermPagoGlosa: str
    FchVenc: str

class Emisor(BaseModel):
    RUTEmisor: str
    RznSoc: str
    GiroEmis: str
    Acteco: str
    DirOrigen: str
    CmnaOrigen: str
    CiudadOrigen: str

class Receptor(BaseModel):
    RUTRecep: str
    RznSocRecep: str
    GiroRecep: str
    CorreoRecep: str
    DirRecep: str
    CmnaRecep: str
    CiudadRecep: str

class Totales(BaseModel):
    MntNeto: str
    MntExe: str
    TasaIVA: str
    IVA: str
    MntTotal: str

class Encabezado(BaseModel):
    IdDoc: IdDoc
    Emisor: Emisor
    Receptor: Receptor
    Totales: Totales

# Estructura para los detalles del documento
class DetalleItem(BaseModel):
    NroLinDet: int
    CdgItem: Dict[str, str]
    NmbItem: str
    DscItem: str
    QtyItem: str
    UnmdItem: str
    PrcItem: str
    MontoItem: str

# Estructura principal del documento
class DteData(BaseModel):
    Encabezado: Encabezado
    Detalles: List[DetalleItem]

class DteSend(BaseModel):
    Dte: List[DteData]

class DteRequest(BaseModel):
    DteSend: DteSend