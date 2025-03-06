from fastapi import APIRouter, Depends, HTTPException
import requests
from app.dependencies import obtener_token
from app.config import WEBFACTURA_API_URL

router = APIRouter(prefix="/dte", tags=["DTE"])

@router.post("/enviar/")
def enviar_dte(dte_data: dict, token: str = Depends(obtener_token)):
    """Envía un Documento Tributario Electrónico (DTE) a WebFactura."""
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    url = f"{WEBFACTURA_API_URL}/api/v3/pos/dte/sendDTEJson.json"
    response = requests.post(url, json=dte_data, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail=response.text)
