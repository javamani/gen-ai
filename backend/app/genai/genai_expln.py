"""
Generate human-readable KYC approval / rejection explanations
using open-source HuggingFace LLM
"""

from transformers import pipeline

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

llm = pipeline(
    "text-generation",
    model=MODEL_NAME,
    device_map="auto",
    max_new_tokens=400
)

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
    
def generate_kyc_explanation(
    extracted_data: dict,
    risk_score: int,
    compliance_rules: list
):
    decision = "REJECTED" if risk_score >= 60 else "APPROVED"

    prompt = f"""
You are a banking compliance officer.

KYC Decision: {decision}

Extracted Customer Data:
{extracted_data}

Calculated Risk Score: {risk_score}

Relevant RBI KYC Compliance Rules:
{compliance_rules}

Explain clearly:
- Why the case was {decision}
- What rules were satisfied or violated
- What corrective action (if any) is required

Use professional banking language.
"""

    response = llm(prompt)
    return response[0]["generated_text"]
