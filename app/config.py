import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

WEBFACTURA_API_URL = os.getenv("WEBFACTURA_API_URL", "https://api-qa.webfactura.cl")
CLIENT_ID = os.getenv("CLIENT_ID", "tu_client_id")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "tu_client_secret")
