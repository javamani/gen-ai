# app/auth/service.py

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

# ----------------------------
# Dummy user store
# ----------------------------
DUMMY_USERS = {
    "maker001": {"username": "maker001", "role": "MAKER", "password": "pass123"},
    "checker001": {"username": "checker001", "role": "CHECKER", "password": "pass123"},
}

# OAuth2 placeholder
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# ----------------------------
# Get current user (for RBAC)
# ----------------------------
def get_current_user(token: str = Depends(oauth2_scheme)):
    if token == "checker-token":
        return {"user_id": "checker001", "role": "CHECKER"}
    return {"user_id": "maker001", "role": "MAKER"}

# ----------------------------
# Fetch user by username
# ----------------------------
def fetch_user(username: str):
    user = DUMMY_USERS.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": user["username"], "role": user["role"], "user_id": user["username"]}

# ----------------------------
# Login endpoint
# ----------------------------
def login_user(username: str, password: str):
    user = DUMMY_USERS.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"username": user["username"], "role": user["role"], "user_id": user["username"]}

