from typing import List

from django.urls import URLPattern
from rest_framework.routers import DefaultRouter

from core.views import EmailsViewSet

app_name = "core"

router = DefaultRouter()
router.register(r"emails", EmailsViewSet)

urlpatterns: List[URLPattern] = []
urlpatterns += router.urls
