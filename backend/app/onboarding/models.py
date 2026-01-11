from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CustomerProfile(BaseModel):
    name: str
    dob: str
    address: str

class KYCApplication(BaseModel):
    id: Optional[str] = None
    customer: CustomerProfile
    maker_id: str
    document_path: Optional[str] = None
    status: str = "DRAFT"
    created_at: datetime = datetime.utcnow()
