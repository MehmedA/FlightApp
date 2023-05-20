from django.db import models
from django.contrib.auth.models import User


class Flight(models.Model):
    flight_No = models.CharField(max_length=64)
    airline = models.CharField(max_length=64)
    departure = models.IntegerField()
    arrival = models.IntegerField()
    departure_date = models.DateTimeField(auto_now=True)
    arrival_date = models.DateTimeField(auto_now=True)
    created_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.flight_No


class Passenger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    created_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Reservations(models.Model):
    flight_ID = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_ID = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    created_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    created_Time = models.DateTimeField(auto_now_add=True)
    updated_Time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.flight_ID} - {self.passenger_ID}"
