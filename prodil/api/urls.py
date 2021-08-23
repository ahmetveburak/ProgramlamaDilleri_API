from django.contrib.auth import views as auth_views
from django.urls import path
from prodil.api.views import BotUserViewSet, ResourceViewSet

urlpatterns = [
    path("resources/", ResourceViewSet.as_view({"get": "list"}), name="resource-list"),
    path("user/", BotUserViewSet.as_view({"post": "create", "get": "list"}), name="create-user"),
]
