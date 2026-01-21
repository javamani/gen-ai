import os
from ocr.service import extract_text_from_document
from nlp.service import extract_entities

UPLOAD_DIR = "uploads"

async def process_kyc(file):
    # Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # OCR
    text = extract_text_from_document(file.filename)

    # NLP
    entities = extract_entities(text)

    return {
        "filename": file.filename,
        "raw_text": text,
        "entities": entities
    }
