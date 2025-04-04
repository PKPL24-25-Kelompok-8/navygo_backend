from django.urls import path
from .views import TopUpAPIView

urlpatterns = [
    path('api/topup/', TopUpAPIView.as_view(), name='topup'),
]