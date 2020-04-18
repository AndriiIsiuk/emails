from django.urls import path, include

urlpatterns = [path("api/core/", include("core.urls", namespace="core"))]
