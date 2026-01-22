from pydantic import BaseModel
from typing import List
from datetime import date

class Document(BaseModel):
    doc_type: str   # PAN, Aadhaar, Passport
    filename: str
    url: str        # file path or storage URL

class CustomerCase(BaseModel):
    case_id: str | None = None
    maker_id: str
    name: str
    dob: date
    address: str
    documents: List[Document] = []
    status: str = "DRAFT"
