from fastapi import APIRouter
from .service import submit_case, checker_decision

router = APIRouter(prefix="/workflow")

@router.post("/submit/{case_id}")
def submit(case_id: str):
    submit_case(case_id)
    return {"status": "SUBMITTED"}

@router.post("/decision/{case_id}")
def decide(case_id: str, decision: str):
    checker_decision(case_id, decision)
    return {"final_status": decision}
