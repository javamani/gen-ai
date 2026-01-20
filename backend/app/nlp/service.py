import re

def clean_text(text: str):
    text = text.replace("\\n", "\n")
    text = text.replace("  ", " ")
    return text.strip()


def detect_document(text: str):
    text_upper = text.upper()

    if "INCOME TAX" in text_upper or "PERMANENT ACCOUNT NUMBER" in text_upper:
        return "PAN"

    if "AADHAAR" in text_upper or "DOB" in text_upper or re.search(r"\d{4}\s\d{4}\s\d{4}", text):
        return "AADHAAR"

    return "UNKNOWN"


def extract_pan(text: str):
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    pan = None
    dob = None
    name = None
    father = None

    # PAN number
    pan_match = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]", text)
    if pan_match:
        pan = pan_match.group()

    # DOB
    dob_match = re.search(r"\d{2}/\d{2}/\d{4}", text)
    if dob_match:
        dob = dob_match.group()

    # Name & Father name usually appear before DOB
    for i in range(len(lines)):
        if dob and dob in lines[i]:
            if i >= 2:
                father = lines[i-1]
                name = lines[i-2]
            break

    return {
        "document_type": "PAN",
        "name": name,
        "father_name": father,
        "dob": dob,
        "pan": pan
    }


def extract_aadhaar(text: str):
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    aadhaar = None
    dob = None
    gender = None
    name = None

    # Aadhaar number
    aadhaar_match = re.search(r"\d{4}\s\d{4}\s\d{4}", text)
    if aadhaar_match:
        aadhaar = aadhaar_match.group()

    # DOB
    dob_match = re.search(r"\d{2}/\d{2}/\d{4}", text)
    if dob_match:
        dob = dob_match.group()

    # Gender
    if "FEMALE" in text.upper():
        gender = "FEMALE"
    elif "MALE" in text.upper():
        gender = "MALE"

    # Name usually appears just before DOB
    for i in range(len(lines)):
        if dob and dob in lines[i]:
            if i > 0:
                name = lines[i-1]
            break

    return {
        "document_type": "AADHAAR",
        "name": name,
        "dob": dob,
        "aadhaar": aadhaar,
        "gender": gender
    }


def extract_entities(text: str):
    text = clean_text(text)
    doc_type = detect_document(text)

    if doc_type == "PAN":
        return extract_pan(text)

    if doc_type == "AADHAAR":
        return extract_aadhaar(text)

    return {"error": "Unknown document"}
