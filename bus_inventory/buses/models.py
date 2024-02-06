from django.db import models

class Bus(models.Model):
    bus_number = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    seats = models.IntegerField()
    trip = models.CharField(max_length=255)
    trip_duration = models.DurationField()
    conductor = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)

    def __str__(self):
        return self.bus_number
