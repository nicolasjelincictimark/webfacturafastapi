from pydantic import BaseModel
from typing import List

class IdDoc(BaseModel):
    TipoDTE: str
    Folio: str
    FchEmis: str
    FmaPago: str
    FchVenc: str

class Emisor(BaseModel):
    RUTEmisor: str
    RznSoc: str
    GiroEmis: str
    CorreoEmisor: str
    Acteco: str
    DirOrigen: str
    CmnaOrigen: str

class Receptor(BaseModel):
    RUTRecep: str
    RznSocRecep: str
    GiroRecep: str
    Contacto: str
    CorreoRecep: str
    DirRecep: str
    CmnaRecep: str

class Totales(BaseModel):
    MntNeto: str
    TasaIVA: str
    IVA: str
    MntTotal: str

class Encabezado(BaseModel):
    IdDoc: IdDoc
    Emisor: Emisor
    Receptor: Receptor
    Totales: Totales

class Detalle(BaseModel):
    NroLinDet: str
    NmbItem: str
    DscItem: str
    QtyItem: str
    UnmdItem: str
    PrcItem: str
    MontoItem: str

class DteItem(BaseModel):
    Encabezado: Encabezado
    Detalle: List[Detalle]  # ✅ AHORA ES UNA LISTA
    _ID: str

class DTE(BaseModel):
    Dte: List[DteItem]  # ✅ AHORA ES UNA LISTA
    _xmlns: str
    _version: str

class DteRequest(BaseModel):
    DTE: DTE
