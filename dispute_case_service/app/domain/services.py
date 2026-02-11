from datetime import datetime
from .models import DisputeCase
from .enums import DisputeStatus

def open_dispute(case_id: str, merchant_id: str, amount: float) -> DisputeCase:
    if amount <= 0:
        raise ValueError("Dispute amount must be greater than zero")

    return DisputeCase(
        case_id=case_id,
        merchant_id=merchant_id,
        amount=amount,
        status=DisputeStatus.OPEN,
        created_at=datetime.utcnow(),
    )
