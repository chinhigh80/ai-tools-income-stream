from fastapi import FastAPI
from app.routes import checkout, webhook

app = FastAPI(title="AI Tools Micro‑Tool", version="0.1.0")

app.include_router(checkout.router, prefix="/checkout", tags=["checkout"])
app.include_router(webhook.router, prefix="/webhook", tags=["webhook"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Tools Micro‑Tool API"}