from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class TemperatureMeasurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    temperature = models.FloatField()
    measured_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor.name} - {self.temperature}°C at {self.measured_at}'