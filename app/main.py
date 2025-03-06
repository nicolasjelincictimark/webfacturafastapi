from fastapi import FastAPI
from app.routers import dte

app = FastAPI()

# Incluir rutas
app.include_router(dte.router)

@app.get("/")
def home():
    return {"message": "API de Integración Odoo - WebFactura"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)