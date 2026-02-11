from django.urls import path
from .views import create_dispute_view

urlpatterns = [
    path("disputes/", create_dispute_view),
]
