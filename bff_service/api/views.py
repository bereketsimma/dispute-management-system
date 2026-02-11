import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from application.create_dispute_flow import create_dispute_flow
from api.serializer import validate_create_dispute_payload


@csrf_exempt
def create_dispute_bff(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)

    try:
        validated_payload = validate_create_dispute_payload(data)
    except ValueError as validation_error:
        return JsonResponse({"error": str(validation_error)}, status=400)

    try:
        dispute = create_dispute_flow(
            case_id=validated_payload.case_id,
            merchant_id=validated_payload.merchant_id,
            amount=validated_payload.amount,
        )
    except ConnectionError:
        return JsonResponse(
            {"error": "Dispute case service is unavailable"}, status=503
        )
    except RuntimeError as downstream_error:
        error_payload = downstream_error.args[0] if downstream_error.args else {}
        if not isinstance(error_payload, dict):
            error_payload = {"error": str(downstream_error)}
        return JsonResponse(error_payload, status=502)

    return JsonResponse(dispute, status=201)
