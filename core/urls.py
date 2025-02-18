from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("apis/", include("apis.urls")),
    path("accounts/", include("accounts.urls")),
    # allauth must come after if we want to customize login page
    path("accounts/", include("allauth.urls")),
    path("parkings/", include("parkings.urls")),
]
