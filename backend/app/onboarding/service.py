import os
import shutil
from fastapi import UploadFile, HTTPException

UPLOAD_DIR = "uploads"
ALLOWED_EXTENSIONS = ["pdf", "jpg", "jpeg", "png"]

# Create uploads directory if not exists
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_uploaded_file(file: UploadFile):
    filename = file.filename
    extension = filename.split(".")[-1].lower()

    # Validate file type
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only PDF, JPG, PNG are allowed."
        )

    file_path = os.path.join(UPLOAD_DIR, filename)

    # Save file temporarily
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": filename,
        "path": file_path,
        "status": "uploaded"
    }
