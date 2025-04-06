from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, OceanViewSet, PortViewSet

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'oceans', OceanViewSet)
router.register(r'ports', PortViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
