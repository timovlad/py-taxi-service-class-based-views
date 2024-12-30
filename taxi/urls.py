from xml.etree.ElementInclude import include

from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls

from .views import index, ManufacturerListView, CarListView, DriverListView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturer/", ManufacturerListView.as_view(), name="manufacturer"),
    path("car/", CarListView.as_view(), name="car"),
    path("driver/", DriverListView.as_view(), name="driver"),
]
app_name = "taxi"
