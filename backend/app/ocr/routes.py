from fastapi import APIRouter, UploadFile, File
from .service import extract_text_from_image

router = APIRouter(prefix="/ocr", tags=["OCR"])

@router.post("/extract")
async def extract_text(file: UploadFile = File(...)):
    file_bytes = await file.read()
    text = extract_text_from_image(file_bytes)
    return {"text": text}
