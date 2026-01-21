from fastapi import APIRouter
from ocr.service import extract_text_from_document

router = APIRouter(prefix="/ocr", tags=["OCR"])

@router.post("/extract-text")
def extract_text(filename: str):
    return {"text": extract_text_from_document(filename)}
