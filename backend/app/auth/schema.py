from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    MAKER = "MAKER"
    CHECKER = "CHECKER"

class LoginRequest(BaseModel):
    username: str
    role: UserRole

class UserResponse(BaseModel):
    username: str
    role: UserRole

