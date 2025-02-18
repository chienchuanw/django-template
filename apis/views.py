from django.http import JsonResponse
from django.conf import settings


def get_map_id(request):
    return JsonResponse(
        {
            "mapId": settings.GOOGLE_MAPS_ID,
        }
    )
