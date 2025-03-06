import requests
from fastapi import HTTPException
from app.config import WEBFACTURA_API_URL, CLIENT_ID, CLIENT_SECRET

def obtener_token():
    """Obtiene un token de autenticación desde WebFactura."""
    url = f"{WEBFACTURA_API_URL}/oauth/v2/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["access_token"]
    raise HTTPException(status_code=400, detail="Error al obtener el token")
