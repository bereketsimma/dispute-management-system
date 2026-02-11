from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


@dataclass
class CreateDisputeInput:
    case_id: str
    merchant_id: str
    amount: str


def validate_create_dispute_payload(payload: dict) -> CreateDisputeInput:
    required_fields = ("case_id", "merchant_id", "amount")
    missing_fields = [field for field in required_fields if field not in payload]

    if missing_fields:
        missing = ", ".join(missing_fields)
        raise ValueError(f"Missing required fields: {missing}")

    case_id = str(payload["case_id"]).strip()
    merchant_id = str(payload["merchant_id"]).strip()
    amount = str(payload["amount"]).strip()

    if not case_id:
        raise ValueError("case_id cannot be empty")

    if not merchant_id:
        raise ValueError("merchant_id cannot be empty")

    try:
        parsed_amount = Decimal(amount)
    except (InvalidOperation, TypeError):
        raise ValueError("amount must be a valid number")

    if parsed_amount <= 0:
        raise ValueError("amount must be greater than 0")

    return CreateDisputeInput(case_id=case_id, merchant_id=merchant_id, amount=str(parsed_amount))
