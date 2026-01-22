from app.db.mongo import db
from app.onboarding.models import CustomerCase
from app.config import UPLOAD_DIR
from uuid import uuid4
import os
from datetime import date, datetime

def create_kyc_case(case_data: CustomerCase) -> str:
    """Create a new onboarding case"""
    case_data.case_id = str(uuid4())
    case_data.status = "DRAFT"
   
    payload = case_data.dict()

    # 🔑 FIX: Convert date fields for MongoDB
    if isinstance(payload.get("dob"), date):
        payload["dob"] = payload["dob"].isoformat()
        # alternatively:
        # payload["dob"] = datetime.combine(payload["dob"], datetime.min.time())

    payload["created_at"] = datetime.utcnow()

    db.cases.insert_one(payload)
    return case_data.case_id

def get_case(case_id: str) -> dict:
    """Fetch a case by case_id"""
    case = db.cases.find_one({"case_id": case_id})
    if case:
        case["_id"] = str(case["_id"])  # Convert ObjectId to string
    return case

def add_document(case_id: str, doc_type: str, file) -> str:
    """Save uploaded document and link to case"""
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    filepath = os.path.join(UPLOAD_DIR, f"{case_id}_{file.filename}")
    with open(filepath, "wb") as f:
        f.write(file.file.read())

    db.cases.update_one(
        {"case_id": case_id},
        {"$push": {"documents": {"doc_type": doc_type, "filename": file.filename, "url": filepath}}}
    )
    return filepath
