# backend/app/workflow/service.py

from datetime import datetime
from app.auth.service import fetch_user
from app.workflow.models import upsert_case, get_case
from app.workflow.models import get_cases_by_status
from app.workflow.schema import KYCStatus
from bson import ObjectId

# ----------------------------
# Helper to serialize MongoDB case document to JSON
# ----------------------------
def serialize_case(case: dict) -> dict:
    case = case.copy()
    # Convert ObjectId to string
    if "_id" in case and isinstance(case["_id"], ObjectId):
        case["_id"] = str(case["_id"])
    # Convert datetime in audit to ISO string
    if "audit" in case:
        for entry in case["audit"]:
            if "time" in entry and isinstance(entry["time"], datetime):
                entry["time"] = entry["time"].isoformat()
    return case

# ----------------------------
# Submit case (MAKER)
# ----------------------------
def submit_case(case_id: str, username: str):
    user = fetch_user(username)
    if not user or user["role"] != "MAKER":
        raise Exception("Only MAKER can submit cases")

    case = get_case(case_id)
    if not case:
        raise Exception("Case not found")

    # Update status and audit
    audit = case.get("audit", [])
    audit.append({
        "action": KYCStatus.SUBMITTED,
        "by": username,
        "time": datetime.utcnow()
    })

    case.update({
        "status": KYCStatus.SUBMITTED,
        "maker": username,
        "audit": audit
    })

    upsert_case(case)
    return serialize_case(case)

# ----------------------------
# Get all submitted cases (for CHECKER)
# ----------------------------
def get_submitted_cases():
    # fetch all cases with status SUBMITTED
    cases = get_cases_by_status("SUBMITTED")
    return list(cases) if cases else []

# ----------------------------
# Approve case (CHECKER)
# ----------------------------
def approve_case(case_id: str, username: str):
    user = fetch_user(username)
    case = get_case(case_id)

    if not user or user["role"] != "CHECKER":
        raise Exception("Only CHECKER can approve")

    if case["maker"] == username:
        raise Exception("Segregation of duties violated")

    audit = case.get("audit", [])
    audit.append({
        "action": KYCStatus.APPROVED,
        "by": username,
        "time": datetime.utcnow()
    })

    case.update({
        "status": KYCStatus.APPROVED,
        "checker": username,
        "audit": audit
    })

    upsert_case(case)
    return serialize_case(case)

# ----------------------------
# Reject case (CHECKER)
# ----------------------------
def reject_case(case_id: str, username: str):
    user = fetch_user(username)
    case = get_case(case_id)

    if not user or user["role"] != "CHECKER":
        raise Exception("Only CHECKER can reject")

    if case["maker"] == username:
        raise Exception("Segregation of duties violated")

    audit = case.get("audit", [])
    audit.append({
        "action": KYCStatus.REJECTED,
        "by": username,
        "time": datetime.utcnow()
    })

    case.update({
        "status": KYCStatus.REJECTED,
        "checker": username,
        "audit": audit
    })

    upsert_case(case)
    return serialize_case(case)
