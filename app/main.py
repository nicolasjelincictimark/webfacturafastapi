from fastapi import FastAPI
from app.api import dte

app = FastAPI(title="Webfactura API", description="API para integración con Webfactura", version="1.0")

# Incluir los routers
app.include_router(dte.router, prefix="/api/v1", tags=["DTE"])

@app.get("/")
def read_root():
    return {"message": "API de integración con Webfactura en funcionamiento"}
