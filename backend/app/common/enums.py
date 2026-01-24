from enum import Enum

class UserRole(str, Enum):
    MAKER = "MAKER"
    CHECKER = "CHECKER"

class KYCStatus(str, Enum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
class DocumentType(str, Enum):  
    PASSPORT = "PASSPORT"
    DRIVER_LICENSE = "DRIVER_LICENSE"
    ID_CARD = "ID_CARD"
class ReviewOutcome(str, Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
class AuditAction(str, Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    SUBMIT = "SUBMIT"
    REVIEW = "REVIEW"       
