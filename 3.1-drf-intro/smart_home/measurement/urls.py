from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, TemperatureMeasurementViewSet

router = DefaultRouter()
router.register(r'sensors', SensorViewSet, basename='sensor')
router.register(r'measurements', TemperatureMeasurementViewSet, basename='measurement')

urlpatterns = [
    path('', include(router.urls)),
]