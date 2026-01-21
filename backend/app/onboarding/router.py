from fastapi import APIRouter, UploadFile, File
from onboarding.service import save_uploaded_file

router = APIRouter(
    prefix="/onboarding",
    tags=["Onboarding"]
)

@router.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload PAN / Aadhaar / Passport document.
    Validates file type and stores file temporarily for OCR processing.
    """
    return save_uploaded_file(file)
