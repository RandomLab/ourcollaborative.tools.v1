from rest_framework.viewsets import ReadOnlyModelViewSet

from pages.models import Information
from pages.api.serializers import InformationSerializer


class InformationViewSet(ReadOnlyModelViewSet):

    serializer_class = InformationSerializer

    def get_queryset(self):
        return Information.objects.order_by("order")
