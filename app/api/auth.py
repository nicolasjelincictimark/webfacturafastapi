import requests
from fastapi import HTTPException
from app.config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL

def get_access_token():
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
    }
    response = requests.get(TOKEN_URL, params=params)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise HTTPException(status_code=400, detail="Error obteniendo token")
