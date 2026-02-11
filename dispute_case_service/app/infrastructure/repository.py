from app.infrastructure.models import DisputeCaseORM
from app.domain.models import DisputeCase
from app.domain.enums import DisputeStatus

class DisputeRepository:

    def save(self, dispute: DisputeCase) -> DisputeCase:
        obj = DisputeCaseORM.objects.create(
            case_id=dispute.case_id,
            merchant_id=dispute.merchant_id,
            amount=dispute.amount,
            status=dispute.status.value,
            created_at=dispute.created_at,
        )
        return dispute
