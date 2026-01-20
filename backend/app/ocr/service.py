import os
import pytesseract
import cv2

UPLOAD_DIR = "uploads"

def extract_text_from_document(filename: str) -> str:
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError("Uploaded file not found")

    img = cv2.imread(file_path)
    if img is None:
        raise Exception("Unable to read image file")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    return text.strip()
