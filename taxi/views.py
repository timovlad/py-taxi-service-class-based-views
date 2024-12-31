from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.shortcuts import render
from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)

class ManufacturerListView(generic.ListView):
    model = Manufacturer
    # template_name = "templates/taxi/manufacturer_list.html"


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")

class DriverListView(generic.ListView):
    model = Driver

def cardetailview(request: HttpRequest, pk: int) -> HttpResponse:
    car = Car.objects.get(id=pk)
    context = {
        "car": car,
    }
    return render(request, "taxi/car_detail.html", context=context)
