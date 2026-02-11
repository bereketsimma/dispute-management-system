import os

from infrastructure.dispute_client import DisputeCaseClient


DEFAULT_DISPUTE_CASE_URL = "http://localhost:8001/api"


def create_dispute_flow(*, case_id: str, merchant_id: str, amount: str) -> dict:
    client = DisputeCaseClient(
        base_url=os.getenv("DISPUTE_CASE_SERVICE_URL", DEFAULT_DISPUTE_CASE_URL)
    )
    return client.create_dispute(case_id=case_id, merchant_id=merchant_id, amount=amount)
