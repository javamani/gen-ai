import os

def save_file(file, case_id: str, upload_dir: str = "./uploads") -> str:
    """Save uploaded file and return path"""
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    filepath = os.path.join(upload_dir, f"{case_id}_{file.filename}")
    with open(filepath, "wb") as f:
        f.write(file.file.read())
    return filepath
