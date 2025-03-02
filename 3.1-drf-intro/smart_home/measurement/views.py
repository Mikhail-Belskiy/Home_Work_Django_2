# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor, TemperatureMeasurement
from .serializers import SensorSerializer, TemperatureMeasurementSerializer

class SensorViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            sensor = Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)

class TemperatureMeasurementViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = TemperatureMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)