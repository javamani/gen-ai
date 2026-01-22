from pymongo import MongoClient
from app.config import MONGO_URL

# Initialize MongoDB client
client = MongoClient(MONGO_URL)

# Database for KYC onboarding
db = client["genai_kyc_db"]
