from app.domain.services import open_dispute
from app.infrastructure.repository import DisputeRepository

def create_dispute(case_id: str, merchant_id: str, amount: float):
    dispute = open_dispute(
        case_id=case_id,
        merchant_id=merchant_id,
        amount=amount,
    )

    repo = DisputeRepository()
    return repo.save(dispute)
