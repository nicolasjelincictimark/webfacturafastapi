import requests
from fastapi import APIRouter, HTTPException
from app.api.auth import get_access_token
from app.config import SEND_DTE_URL
from app.models.dte_model import DteRequest

router = APIRouter()

@router.post("/enviar-dte")
def enviar_dte(dte_data: DteRequest):
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(SEND_DTE_URL, json=dte_data.dict(), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=400, detail="Error enviando DTE")
