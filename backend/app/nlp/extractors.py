import re

# ---------- PAN EXTRACTOR ----------

def extract_pan(text: str):
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    pan_pattern = r"[A-Z]{5}[0-9]{4}[A-Z]"
    dob_pattern = r"\d{2}/\d{2}/\d{4}"

    pan = re.search(pan_pattern, text)
    dob = re.search(dob_pattern, text)

    name = None
    father_name = None

    # PAN cards usually have:
    # Line1: GOVT OF INDIA
    # Line2: NAME
    # Line3: FATHER NAME
    # Line4: DOB

    for i, line in enumerate(lines):
        if "GOVT" in line.upper() and i+2 < len(lines):
            name = lines[i+1]
            father_name = lines[i+2]
            break

    return {
        "document_type": "PAN",
        "name": name,
        "father_name": father_name,
        "dob": dob.group() if dob else None,
        "pan": pan.group() if pan else None
    }


# ---------- AADHAAR EXTRACTOR ----------

def extract_aadhaar(text: str):
    aadhaar_pattern = r"\d{4}\s\d{4}\s\d{4}"
    dob_pattern = r"\d{2}/\d{2}/\d{4}"

    aadhaar = re.search(aadhaar_pattern, text)
    dob = re.search(dob_pattern, text)

    gender = None
    if "FEMALE" in text.upper():
        gender = "FEMALE"
    elif "MALE" in text.upper():
        gender = "MALE"

    name = None

    # Aadhaar name is usually before DOB line
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    for i, line in enumerate(lines):
        if "DOB" in line.upper() and i > 0:
            name = lines[i-1]
            break

    return {
        "document_type": "AADHAAR",
        "name": name,
        "dob": dob.group() if dob else None,
        "aadhaar": aadhaar.group() if aadhaar else None,
        "gender": gender
    }
