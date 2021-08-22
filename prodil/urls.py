from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("resources/", views.ResourceListView.as_view(), name="resources"),
    path("resources/new/", views.ResourceCreateView.as_view(), name="new-res"),
    path("resources/<int:pk>/", views.ResourceDetailView.as_view(), name="detail-res"),
    path("resources/<int:pk>/delete/", views.ResourceDeleteView.as_view(), name="del-res"),
    path("resources/edit/<int:pk>/", views.ResourceEditView.as_view(), name="edit-res"),
    path("login/", auth_views.LoginView.as_view(template_name="prodil/registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="prodil/registration/logout.html"), name="logout"),
]
