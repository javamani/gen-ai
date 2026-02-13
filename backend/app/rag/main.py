from fastapi import FastAPI
from app.rag.compliance import router as compliance_router

app = FastAPI(title="AI KYC Compliance Platform")

app.include_router(compliance_router)
