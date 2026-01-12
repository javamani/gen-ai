from fastapi import FastAPI

# Create FastAPI app FIRST
app = FastAPI(title="AI-Driven KYC Onboarding System")

# Import routers AFTER app is created
from app.onboarding.routes import router as onboarding_router
from app.workflow.routes import router as workflow_router
from app.ocr.routes import router as ocr_router

# Register routers
app.include_router(onboarding_router)
app.include_router(workflow_router)
app.include_router(ocr_router)

# Health check endpoint
@app.get("/")
def health_check():
    return {"status": "KYC system running"}
