from fastapi import APIRouter, UploadFile, File
from pipeline.service import process_kyc

router = APIRouter(prefix="/pipeline", tags=["Pipeline"])

@router.post("/kyc-process")
async def kyc(file: UploadFile = File(...)):
    return await process_kyc(file)
