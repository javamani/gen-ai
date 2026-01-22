from fastapi import APIRouter, UploadFile, File, HTTPException
from app.onboarding.models import CustomerCase
from app.onboarding.service import create_kyc_case, get_case, add_document

router = APIRouter(prefix="/onboarding", tags=["Onboarding"])


# ✅ CREATE CASE
@router.post("/create")
def create_customer_case(case: CustomerCase):
    case_id = create_kyc_case(case)
    return {
        "case_id": case_id,
        "status": "DRAFT"
    }


# ✅ GET CASE
@router.get("/{case_id}")
def get_customer_case(case_id: str):
    case = get_case(case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return case


# ✅ UPLOAD DOCUMENT
@router.post("/{case_id}/documents")
def upload_document(
    case_id: str,
    file: UploadFile = File(...),
    doc_type: str = "PAN"
):
    filepath = add_document(case_id, doc_type, file)
    return {
        "message": "Document uploaded",
        "file_path": filepath
    }
