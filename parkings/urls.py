from django.urls import path
from parkings.views import ParkingIndexView, ParkingDetailView

app_name = "parkings"

urlpatterns = [
    path("", ParkingIndexView.as_view(), name="index"),
    path("detail/", ParkingDetailView.as_view(), name="detail"),
]
