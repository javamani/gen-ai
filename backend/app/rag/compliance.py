from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.rag_engine import retrieve_compliance_rules
from app.genai.genai_expln import generate_kyc_explanation

router = APIRouter(prefix="/compliance", tags=["Compliance"])

class ComplianceRequest(BaseModel):
    extracted_data: dict
    risk_score: int


@router.post("/evaluate")
def evaluate_kyc(request: ComplianceRequest):
    """
    Orchestrates:
    1. RAG-based RBI rule retrieval
    2. GenAI explanation
    """

    query = "KYC compliance verification based on extracted identity data"

    rules = retrieve_compliance_rules(query)

    explanation = generate_kyc_explanation(
        extracted_data=request.extracted_data,
        risk_score=request.risk_score,
        compliance_rules=rules
    )

    decision = "REJECTED" if request.risk_score >= 60 else "APPROVED"

    return {
        "decision": decision,
        "risk_score": request.risk_score,
        "compliance_rules": rules,
        "explanation": explanation
    }
