from pydantic import BaseModel

class CustomerCreateRequest(BaseModel):
    name: str
    dob: str
    address: str

class KYCSubmitResponse(BaseModel):
    case_id: str
    status: str
