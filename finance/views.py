from django.shortcuts import render
from rest_framework import generics
from .models import TrNavypay
from .serializers import TopUpSerializer

class TopUpAPIView(generics.CreateAPIView):
    queryset = TrNavypay.objects.all()
    serializer_class = TopUpSerializer
