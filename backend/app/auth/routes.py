from fastapi import APIRouter, HTTPException
from app.auth.schema import LoginRequest, UserResponse
from app.auth.service import login_user, fetch_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=UserResponse)
def login(request: LoginRequest):
    return login_user(request.username, request.role)

@router.get("/me/{username}", response_model=UserResponse)
def get_me(username: str):
    user = fetch_user(username)
    if not user:
        raise HTTPException(404, "User not found")
    return user
