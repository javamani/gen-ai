"""
Application entry point.

- Initializes FastAPI app
- Registers routers for all modules
- Configures middleware
"""

from fastapi import FastAPI

app = FastAPI(title="AI-Driven KYC Onboarding System")

@app.get("/")
def health_check():
    """Health check endpoint"""
    return {"status": "KYC system running"}
