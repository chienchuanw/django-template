from django.urls import path
from parkings.views import ParkingIndexView

app_name = "parkings"

urlpatterns = [
    path("", ParkingIndexView.as_view(), name="index"),
]
