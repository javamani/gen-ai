from .states import *
from app.onboarding.service import get_case

def submit_case(case_id):
    case = get_case(case_id)
    if case.status != DRAFT:
        raise Exception("Invalid state transition")
    case.status = SUBMITTED

def checker_decision(case_id, decision):
    case = get_case(case_id)
    if case.status != AI_REVIEWED:
        raise Exception("Case not ready for checker")
    if decision == "APPROVE":
        case.status = CHECKER_APPROVED
    else:
        case.status = CHECKER_REJECTED
