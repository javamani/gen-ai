from transformers import pipeline
from typing import Dict, List

class GenAIExplanationEngine:
    def __init__(
        self,
        model_name: str = "mistralai/Mistral-7B-Instruct-v0.2"
    ):
        """
        Initialize HuggingFace text generation pipeline
        """
        self.llm = pipeline(
            task="text-generation",
            model=model_name,
            device_map="auto",
            max_new_tokens=300,
            do_sample=False,   # deterministic output (important for audit)
            temperature=0.2
        )

    def _build_prompt(
        self,
        extracted_data: Dict,
        risk_score: float,
        compliance_rules: List[Dict],
        final_decision: str
    ) -> str:
        """
        Build structured prompt for explanation generation
        """

        rules_text = "\n".join(
            [f"- {rule['content']}" for rule in compliance_rules]
        )

        prompt = f"""
You are a banking compliance assistant.

Your task is to EXPLAIN the KYC decision in a clear, professional,
auditor-friendly manner.

Do NOT invent facts.
Do NOT reference internal AI systems.
Base your explanation ONLY on the provided data and RBI rules.

=====================
EXTRACTED KYC DATA
=====================
{extracted_data}

=====================
KYC RISK SCORE
=====================
Risk Score: {risk_score} / 100

=====================
RELEVANT RBI KYC RULES
=====================
{rules_text}

=====================
FINAL HUMAN DECISION
=====================
{final_decision}

=====================
INSTRUCTIONS
=====================
- If approved: explain why risk is acceptable
- If rejected: clearly state deficiencies
- Reference RBI rules where applicable
- Use simple, professional banking language
- Maximum 2 short paragraphs

EXPLANATION:
"""
        return prompt

    def generate_explanation(
        self,
        extracted_data: Dict,
        risk_score: float,
        compliance_rules: List[Dict],
        final_decision: str
    ) -> str:
        """
        Generate explanation text for checker & audit teams
        """

        prompt = self._build_prompt(
            extracted_data,
            risk_score,
            compliance_rules,
            final_decision
        )

        response = self.llm(prompt)[0]["generated_text"]

        # Remove prompt from output (safe cleanup)
        explanation = response.replace(prompt, "").strip()

        return explanation