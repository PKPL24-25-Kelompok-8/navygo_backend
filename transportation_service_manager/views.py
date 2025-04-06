from django.shortcuts import render

from rest_framework import mixins, viewsets
from .models import City, Ocean, Port
from .serializers import CitySerializer, OceanSerializer, PortSerializer
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
 
class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view or edit City Model.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = [JWTStatelessUserAuthentication]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        else:
            return [AllowAny()]

class OceanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view or edit Ocean Model.
    """
    queryset = Ocean.objects.all()
    serializer_class = OceanSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        else:
            return [AllowAny()]

class PortViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view or edit Port Model.
    """
    queryset = Port.objects.select_related('ocean', 'city').all()
    serializer_class = PortSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        else:
            return [AllowAny()]