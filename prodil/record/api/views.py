from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from prodil.record.api.serializers import CategorySerializer, ResourceSerializer
from prodil.record.filters import ResourceFilter
from prodil.record.models import Category, Resource


class ResourcePagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = "page_size"


class ResourceViewSet(ListModelMixin, GenericViewSet):
    serializer_class = ResourceSerializer
    queryset = Resource.objects.filter(enabled=True).order_by("-rating")
    pagination_class = ResourcePagination
    permission_classes = (IsAuthenticated,)
    filterset_class = ResourceFilter


class CategoryViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(enabled=True)
    permission_classes = (IsAuthenticated,)
    lookup_field = "name"
