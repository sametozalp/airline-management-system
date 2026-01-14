from django.db import models
from flights.models import Flight

# Create your models here.

class Reservation(models.Model):
    passenger_name = models.CharField(max_length=200)
    passenger_email = models.CharField(max_length=200)
    reservation_code = models.CharField(max_length=200, unique=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return self.reservation_code + " - " + self.passenger_name