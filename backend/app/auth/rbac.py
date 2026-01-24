from fastapi import Depends, HTTPException
from app.auth.service import get_current_user  # returns dict with keys: user_id, role

def require_role(*allowed_roles):
    """
    FastAPI dependency to enforce role-based access.
    Usage: user = Depends(require_role("MAKER"))
    """
    def role_dependency(current_user=Depends(get_current_user)):
        if current_user["role"] not in allowed_roles:
            raise HTTPException(status_code=403, detail="Forbidden: insufficient privileges")
        return current_user
    return role_dependency
