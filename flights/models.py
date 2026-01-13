from django.db import models
from airplanes.models import Airplane

# Create your models here.

class Flight(models.Model):
    flight_number = models.CharField(max_length=200)
    departure = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)

    def __str__(self):
        return self.departure + " - " + self.destination + " (" + self.flight_number + ")"
