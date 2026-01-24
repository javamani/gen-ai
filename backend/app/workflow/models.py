from app.db.mongo import db

def get_case(case_id: str):
    return db.cases.find_one({"case_id": case_id})

def upsert_case(case: dict):
    db.cases.update_one(
        {"case_id": case["case_id"]},
        {"$set": case},
        upsert=True
    )



def get_cases_by_status(status: str):
    # fetch all cases with the given status
    return list(db.cases.find({"status": status}, {"_id": 0}))
