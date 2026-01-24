# backend/app/workflow/routes.py

from fastapi import APIRouter, HTTPException, Depends
from app.workflow.service import submit_case, approve_case, reject_case, get_submitted_cases
from app.auth.service import get_current_user  # dummy RBAC
from app.workflow.schema import CaseRequest

router = APIRouter(prefix="/workflow", tags=["Workflow"])

# ----------------------------
# Dummy dependency for auth
# ----------------------------
def dummy_auth(token: str = Depends(get_current_user)):
    """
    Use get_current_user from auth/service which returns dict:
    { user_id, role }
    """
    return token

# ----------------------------
# Submit case (MAKER)
# ----------------------------
@router.post("/submit")
def submit(request: CaseRequest, user=Depends(dummy_auth)):
    try:
        case = submit_case(request.case_id, user["user_id"])
        return {"message": "Case submitted successfully", "case": case}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ----------------------------
# Approve case (CHECKER)
# ----------------------------
@router.post("/approve")
def approve(request: CaseRequest, user=Depends(dummy_auth)):
    try:
        case = approve_case(request.case_id, user["user_id"])
        return {"message": "Case approved successfully", "case": case}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ----------------------------
# Reject case (CHECKER)
# ----------------------------
@router.post("/reject")
def reject(request: CaseRequest, user=Depends(dummy_auth)):
    try:
        case = reject_case(request.case_id, user["user_id"])
        return {"message": "Case rejected successfully", "case": case}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# GET all submitted cases (for CHECKER)
@router.get("/cases")
def list_submitted_cases(current_user=Depends(get_current_user)):
    user = current_user  # dummy user returned by get_current_user
    if not user or user["role"] != "CHECKER":
        raise Exception("Only CHECKER can view submitted cases")

    cases = get_submitted_cases()
    # ensure always returning a list
    return cases if cases else []

