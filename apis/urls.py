from django.urls import path
from apis.views import get_map_id

app_name = "apis"

urlpatterns = [
    path("map-id/", get_map_id, name="get_ma_id"),
]
