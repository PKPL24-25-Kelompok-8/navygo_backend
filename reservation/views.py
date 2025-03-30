from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from utils.models import Reservation
from utils.serializers import ReservationSerializer


# Create your views here.
class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def list(self, request: Request):
        pass

    def create(self, request: Request):
        pass
