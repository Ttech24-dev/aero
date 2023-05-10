from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def flight(request):
    return render(request, "flight.html",{
        "flights": Flight.objects.all()
    })
    
def control(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "control.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights= flight).all()
    })
    
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("control", args=(flight.id,)))
