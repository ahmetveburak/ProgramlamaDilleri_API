from prodil.api.serializers import BotUserSerializer, ResourceSerializer
from prodil.models import BotUser, Resource
from prodil.views import ResourceCreateView
from rest_framework import mixins, permissions, viewsets


class ResourceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()
    permission_class = (permissions.IsAuthenticated,)


class BotUserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BotUserSerializer
    queryset = BotUser.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
