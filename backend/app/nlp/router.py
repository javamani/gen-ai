from fastapi import APIRouter
from nlp.service import extract_entities

router = APIRouter(prefix="/nlp", tags=["NLP"])

@router.post("/extract-entities")
def extract(text: str):
    return extract_entities(text)
