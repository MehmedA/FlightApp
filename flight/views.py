from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (Flight, FlightSerializer, Passenger, PassengerSerializer, Reservations, ReservationsSerializer)

class PassengerView(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    
class FlightView(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    
class ReservationsView(ModelViewSet):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer