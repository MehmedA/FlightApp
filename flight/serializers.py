from rest_framework import serializers
from .models import Passenger, Flight, Reservations

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        exclude = []

class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        exclude = []

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        exclude = []

