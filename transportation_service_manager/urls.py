from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, OceanViewSet, PortViewSet, VehicleViewSet, PortVisitViewSet

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'oceans', OceanViewSet)
router.register(r'ports', PortViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'port-visits', PortVisitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
