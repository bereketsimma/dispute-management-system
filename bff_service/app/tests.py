import json
from unittest.mock import patch

from django.test import Client, TestCase


class CreateDisputeBffTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/bff/disputes/create/"

    @patch("api.views.create_dispute_flow")
    def test_create_dispute_success(self, mocked_flow):
        mocked_flow.return_value = {"case_id": "CASE-123", "status": "CREATED"}

        response = self.client.post(
            self.url,
            data=json.dumps(
                {"case_id": "CASE-123", "merchant_id": "M-100", "amount": "10.50"}
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertJSONEqual(
            response.content,
            {"case_id": "CASE-123", "status": "CREATED"},
        )

    def test_create_dispute_rejects_invalid_payload(self):
        response = self.client.post(
            self.url,
            data=json.dumps({"case_id": "", "merchant_id": "M-100", "amount": "10.50"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {"error": "case_id cannot be empty"})

    @patch("api.views.create_dispute_flow")
    def test_create_dispute_when_downstream_unavailable(self, mocked_flow):
        mocked_flow.side_effect = ConnectionError("timeout")

        response = self.client.post(
            self.url,
            data=json.dumps(
                {"case_id": "CASE-123", "merchant_id": "M-100", "amount": "10.50"}
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 503)
        self.assertJSONEqual(
            response.content,
            {"error": "Dispute case service is unavailable"},
        )
