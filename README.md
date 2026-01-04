<<<<<<< HEAD
# AI-Driven KYC Onboarding System

This project implements an AI-powered Know Your Customer (KYC)
onboarding and compliance assistant using open-source technologies.
===============================
FUNCTIONAL REQUIREMENTS
===============================

1. Implement Customer Onboarding:
   - Capture customer profile (Name, DOB, Address).
   - Upload KYC documents (PAN, Aadhaar, Passport).
   - Store cases in MongoDB.
   - Each onboarding case is created by a MAKER user.

2. Implement Role-Based Access Control:
   - Roles: MAKER, CHECKER.
   - MAKER can create and submit KYC cases.
   - CHECKER can review, approve, or reject cases.
   - Enforce segregation of duties.

3. Implement Lightweight Workflow Engine:
   - Case states:
     DRAFT → SUBMITTED → AI_REVIEWED → CHECKER_APPROVED / CHECKER_REJECTED
   - Validate state transitions based on role and action.
   - Maintain an audit trail for all state changes.

4. OCR & Document Processing:
   - Extract text from uploaded documents using PaddleOCR.
   - Support scanned and photographed documents.

5. NLP & Entity Extraction:
   - Extract Name, Date of Birth, Address, PAN/Aadhaar using spaCy and Regex.

6. Validation & Risk Scoring:
   - Compare extracted fields with onboarding data.
   - Calculate a rule-based KYC risk score.
   - Detect anomalies (missing or inconsistent data).

7. RAG-Based Compliance Engine:
   - Ingest RBI KYC Master Direction documents.
   - Use SentenceTransformers for embeddings.
   - Store vectors in FAISS.
   - Retrieve relevant compliance rules using LangChain.

8. GenAI Decision Explanation:
   - Use an open-source LLM (Llama / Mistral / Gemma via HuggingFace).
   - Generate explainable AI reasoning for approval or rejection.

9. Backend API:
   - Build REST APIs using FastAPI.
   - Use MongoDB for persistence.
   - Modular, service-based architecture.
   - Environment variable support.
   - Error handling and logging.

===============================
FRONTEND REQUIREMENTS (REACT)
===============================

- React frontend with:
  - Login screen (Maker / Checker).
  - Maker dashboard:
    - Create KYC case.
    - Upload documents.
    - Submit case for review.
    - View case status.
  - Checker dashboard:
    - View submitted cases.
    - Review AI-extracted data.
    - View risk score and GenAI explanation.
    - Approve or reject cases.
  - Status tracking and audit history.

===============================
TECH STACK (STRICT)
===============================

OCR: PaddleOCR  
NLP: spaCy, Regex  
Embeddings: SentenceTransformers  
Vector DB: FAISS  
LLM: HuggingFace (Llama / Mistral / Gemma)  
RAG: LangChain  
Backend: FastAPI  
Frontend: React  
Database: MongoDB  

===============================
DELIVERABLES
===============================

1. Complete project folder structure.
2. Starter code for:
   - Authentication & role management
   - Onboarding module
   - Workflow engine
   - OCR module
   - NLP entity extraction
   - Risk scoring
   - RAG compliance engine
   - GenAI explanation
   - MongoDB persistence
3. React component structure for Maker and Checker dashboards.
4. API contracts between frontend and backend.
5. Clear comments explaining each module.
6. Code written in a clean, readable, college-safe manner.