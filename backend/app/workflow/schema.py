from pydantic import BaseModel
from enum import Enum

class KYCStatus(str, Enum):
    SUBMITTED = "SUBMITTED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class CaseRequest(BaseModel):
    case_id: str
    

    
   

