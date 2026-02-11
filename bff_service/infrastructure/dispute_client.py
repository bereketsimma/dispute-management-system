import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class DisputeCaseClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def create_dispute(self, *, case_id: str, merchant_id: str, amount: str) -> dict:
        request_payload = {
            "case_id": case_id,
            "merchant_id": merchant_id,
            "amount": amount,
        }

        request = Request(
            url=f"{self.base_url}/disputes/",
            data=json.dumps(request_payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as error:
            body = error.read().decode("utf-8") if hasattr(error, "read") else ""
            try:
                payload = json.loads(body) if body else {}
            except json.JSONDecodeError:
                payload = {"error": body or "Unable to parse downstream error"}
            raise RuntimeError(payload)
        except URLError as error:
            raise ConnectionError(str(error.reason))
