from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3, null=True)
    city = models.CharField(max_length=64, null=True)
    
    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.origin} to {self.destination}" 

class Passenger(models.Model):
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=300, null=True)
    next_of_kin = models.CharField(max_length=60, null=True)
    kin_phone = models.CharField(max_length=60, null=True)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"