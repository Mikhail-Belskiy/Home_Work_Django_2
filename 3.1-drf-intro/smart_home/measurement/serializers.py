from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from rest_framework import serializers
from .models import Sensor, TemperatureMeasurement

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class TemperatureMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMeasurement
        fields = ['sensor', 'temperature', 'measured_at']