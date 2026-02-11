from django.db import models

class DisputeCaseORM(models.Model):
    case_id = models.CharField(max_length=64, unique=True)
    merchant_id = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=32)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "dispute_cases"
