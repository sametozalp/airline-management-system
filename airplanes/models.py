from django.db import models

# Create your models here.

class Airplane(models.Model):
    tail_number = models.CharField(max_length=200, unique=True)
    model = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField(default=0)
    production_year = models.PositiveIntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.tail_number