from .models import KYCApplication, CustomerProfile
from uuid import uuid4

kyc_db = {}   # temporary in-memory store

def create_kyc_case(customer_data, maker_id):
    case_id = str(uuid4())
    customer = CustomerProfile(**customer_data.dict())
    kyc = KYCApplication(id=case_id, customer=customer, maker_id=maker_id)
    kyc_db[case_id] = kyc
    return kyc

def attach_document(case_id, file_path):
    kyc_db[case_id].document_path = file_path

def get_case(case_id):
    return kyc_db.get(case_id)
