from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from app.application.create_dispute import create_dispute

@csrf_exempt
def create_dispute_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    data = json.loads(request.body)

    dispute = create_dispute(
        case_id=data["case_id"],
        merchant_id=data["merchant_id"],
        amount=float(data["amount"]),
    )

    return JsonResponse({
        "case_id": dispute.case_id,
        "status": dispute.status.value,
    }, status=201)
