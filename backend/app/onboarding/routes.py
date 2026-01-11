from fastapi import APIRouter, UploadFile, File
from .schemas import CustomerCreateRequest
from .service import create_kyc_case, attach_document

router = APIRouter(prefix="/onboarding")

@router.post("/create")
def create_case(request: CustomerCreateRequest):
    maker_id = "maker001"   # later from login
    case = create_kyc_case(request, maker_id)
    return {"case_id": case.id, "status": case.status}

@router.post("/upload/{case_id}")
def upload_document(case_id: str, file: UploadFile = File(...)):
    path = f"uploads/{file.filename}"
    attach_document(case_id, path)
    return {"message": "Document uploaded"}
