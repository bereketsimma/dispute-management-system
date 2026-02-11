from django.urls import path
from .views import create_dispute_bff

urlpatterns = [
    path("disputes/create/", create_dispute_bff),
]

