from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from prodil.record.api.serializers import ResourceSerializer
from prodil.record.models import Resource


class ResourcePagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = "page_size"


class ResourceViewSet(ListModelMixin, GenericViewSet):
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all().order_by("rating")
    pagination_class = ResourcePagination
    permission_classes = (IsAuthenticated,)
