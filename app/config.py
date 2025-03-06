import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID", "TU_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "TU_CLIENT_SECRET")

TOKEN_URL = "https://api-qa.webfactura.cl/oauth/v2/token"
SEND_DTE_URL = "https://api-qa.webfactura.cl/api/v3/pos/dte/sendDTEJson.json"