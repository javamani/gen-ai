from fastapi import FastAPI

# Import routers
from onboarding.router import router as onboarding_router
from ocr.router import router as ocr_router
from nlp.router import router as nlp_router
from pipeline.router import router as pipeline_router

# Create FastAPI app
app = FastAPI(title="AI KYC System")

# Register routers
app.include_router(onboarding_router)
app.include_router(ocr_router)
app.include_router(nlp_router)
app.include_router(pipeline_router)

@app.get("/")
def home():
    return {"message": "AI KYC System is running"}
