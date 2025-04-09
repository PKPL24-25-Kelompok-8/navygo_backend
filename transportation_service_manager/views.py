from django.shortcuts import render

from rest_framework import mixins, viewsets
from .models import City, Ocean, Port, Vehicle, PortVisit, TransportationService, StatusTransportationService
from .serializers import CitySerializer, OceanSerializer, PortSerializer, VehicleSerializer, PortVisitSerializer
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
            # return [IsAuthenticated()]
            return [AllowAny()]
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
            # return [IsAuthenticated()]
            return [AllowAny()]
        else:
            return [AllowAny()]
        
class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view or edit Vehicle Model.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            # return [IsAuthenticated()]
            return [AllowAny()]
        else:
            return [AllowAny()]
        
class PortVisitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view or edit PortVisit Model.
    """
    queryset = PortVisit.objects.select_related('current_vehicle', 'current_port', 'port_destination').all()
    serializer_class = PortVisitSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            # return [IsAuthenticated()]
            return [AllowAny()]
        else:
            return [AllowAny()]
        
class TransportationServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view or edit TransportationService Model.
    """
    queryset = TransportationService.objects.select_related('port_visit', 'status').all()
    serializer_class = PortVisitSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            # return [IsAuthenticated()]
            return [AllowAny()]
        else:
            return [AllowAny()]
        
class StatusTransportationServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view or edit StatusTransportationService Model.
    """
    queryset = StatusTransportationService.objects.all()
    serializer_class = PortVisitSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            # return [IsAuthenticated()]
            return [AllowAny()]
        else:
            return [AllowAny()]