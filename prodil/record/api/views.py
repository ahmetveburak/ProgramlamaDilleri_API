from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from prodil.record.api.serializers import CategorySerializer, ResourceSerializer, ResourceUpdateSerializer
from prodil.record.filters import ResourceFilter
from prodil.record.models import Category, Resource


class ResourcePagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = "page_size"


class ResourceViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = ResourceSerializer
    queryset = Resource.objects.filter(enabled=True).order_by("-rating")
    pagination_class = ResourcePagination
    permission_classes = (IsAuthenticated,)
    filterset_class = ResourceFilter


class ResourceUpdateViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = ResourceUpdateSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Resource.objects.filter(content="DC")
    lookup_field = "file_name"
    lookup_value_regex = "[^/]+"


class CategoryViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(enabled=True)
    permission_classes = (IsAuthenticated,)
    lookup_field = "name"
