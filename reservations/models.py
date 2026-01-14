from django.db import models
from flights.models import Flight
import uuid

def create_reservation_code():
    return str(uuid.uuid4())

# Create your models here.

class Reservation(models.Model):
    passenger_name = models.CharField(max_length=200)
    passenger_email = models.CharField(max_length=200)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reservation_code = models.CharField(max_length=200, default=create_reservation_code, unique=True)

    def __str__(self):
        return self.reservation_code + " - " + self.passenger_name