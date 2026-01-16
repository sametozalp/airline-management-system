from django.db import models
from flights.models import Flight
import uuid

# Create your models here.

class Reservation(models.Model):
    passenger_name = models.CharField(max_length=200)
    passenger_email = models.CharField(max_length=200)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reservation_code = models.CharField(max_length=200, default=str(uuid.uuid4()), unique=True)

    def __str__(self):
        return self.reservation_code + " - " + self.passenger_name
    
    def get_reservation_status_message(self):
        current_status = "Confirmed"
        
        return (
            f"Dear {self.passenger_name},\n\n"
            f"Your reservation has been successfully processed.\n"
            f"------------------------------------------\n"
            f"RESERVATION DETAILS:\n"
            f"Reservation Code: {self.reservation_code}\n"
            f"Flight: {self.flight}\n"
            f"Status: {current_status}\n"
            f"Date: {self.created_at}\n"
            f"------------------------------------------\n\n"
            f"Thank you for choosing us."
        )