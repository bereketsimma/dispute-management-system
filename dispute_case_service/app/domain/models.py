from dataclasses import dataclass
from .enums import DisputeStatus
from datetime import datetime

@dataclass
class DisputeCase:
    case_id: str
    merchant_id: str
    amount: float
    status: DisputeStatus
    created_at: datetime
