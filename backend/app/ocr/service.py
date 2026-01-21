from paddleocr import PaddleOCR
from PIL import Image
import tempfile, os, io
import cv2
import numpy as np
from pdf2image import convert_from_bytes

ocr = PaddleOCR(use_angle_cls=True, lang="en")

def extract_text_from_image(file_bytes: bytes) -> str:
    try:
        # Detect PDF using magic header
        if file_bytes[:4] == b"%PDF":
            images = convert_from_bytes(file_bytes,dpi=300,poppler_path=r"C:\Software\poppler-25.12.0\Library\bin")
            full_text = []
            for img in images:
                full_text.extend(run_ocr(img))
            return "\n".join(full_text)

        # Otherwise treat as image
        image = Image.open(io.BytesIO(file_bytes)).convert("RGB")
        return "\n".join(run_ocr(image))

    except Exception as e:
        return f"OCR processing failed: {str(e)}"


def run_ocr(pil_image):
    # Convert to OpenCV
    img = np.array(pil_image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Auto rotate if height >> width
    h, w = img.shape[:2]
    if h > w * 1.2:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Increase contrast
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # Save temp
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        cv2.imwrite(f.name, gray)
        path = f.name

    result = ocr.ocr(path)
    os.remove(path)

    extracted = []
    for line in result:
        for word in line:
            extracted.append(word[1][0])

    return extracted



