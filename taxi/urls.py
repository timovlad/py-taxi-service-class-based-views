from xml.etree.ElementInclude import include

from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls

from taxi.views import index, ManufacturerListView, CarListView, DriverListView, cardetailview

urlpatterns = [
    path("", index, name="index"),
    path("manufacturer/", ManufacturerListView.as_view(), name="manufacturer"),
    path("car/", CarListView.as_view(), name="car"),
    path("car/<int:pk>/", cardetailview, name="car-detail"),# тут хочу шось таке
    # CarListView.as_view() але для детального вигляду стандартними методами
    path("driver/", DriverListView.as_view(), name="driver"),
]
app_name = "taxi"
