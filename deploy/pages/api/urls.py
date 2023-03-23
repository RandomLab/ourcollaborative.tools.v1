from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from pages.api.views import InformationViewSet

information_router = routers.SimpleRouter()
information_router.register("informations", InformationViewSet, basename="informations")

urlpatterns = [path("", include(information_router.urls))]
