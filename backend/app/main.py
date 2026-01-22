
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.onboarding.router import router as onboarding_router

# Create FastAPI app FIRST
app = FastAPI(title="AI-Driven KYC Onboarding System")

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/onboarding", tags=["Onboarding"])

# Import routers AFTER app is created
from app.onboarding.router import router as onboarding_router
from app.workflow.routes import router as workflow_router
from app.ocr.routes import router as ocr_router


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(onboarding_router)
app.include_router(workflow_router)
app.include_router(ocr_router)

# Health check endpoint

@app.get("/")
def health_check():
    return {"status": "KYC system running"}
