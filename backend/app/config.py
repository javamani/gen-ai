import os

# MongoDB URL (can override via environment variable)
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

# Upload directory
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")