from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from prodil.filters import ResourceFilter
from prodil.forms import ResourceEditForm

from .models import Category, Resource


class UserLoginView(LoginView):
    template_name: str = "prodil/registration/login.html"


class UserLogoutView(LogoutView):
    template_name: str = "prodil/registration/logout.html"


class IndexView(TemplateResponseMixin, View):
    template_name: str = "prodil/index.html"

    def get(self, request, *args, **kwargs):
        """Get all Categories and divide by 3"""

        CATGS = Category.objects.all()
        COLS = 3
        catgs_divide_by_three = [CATGS[i : i + COLS] for i in range(0, len(CATGS), COLS)]

        return self.render_to_response(
            {
                "section": "prodil",
                "catgs": catgs_divide_by_three,
            },
        )


class ResourceListView(ListView):
    template_name = "prodil/res_list.html"
    model = Resource

    def get_queryset(self):
        queryset = super().get_queryset()
        res_filter = ResourceFilter(self.request.GET, queryset)
        return res_filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        res_filter = ResourceFilter(self.request.GET, queryset)
        context["filter"] = res_filter
        return context


class ResourceCreateView(LoginRequiredMixin, CreateView):
    model = Resource
    template_name = "prodil/create.html"
    exclude = ("file_id",)


class ResourceDeleteView(LoginRequiredMixin, DeleteView):
    model = Resource
    success_url = reverse_lazy("resources")
    template_name = "prodil/delete.html"


class ResourceEditView(LoginRequiredMixin, UpdateView):
    model = Resource
    form_class = ResourceEditForm
    success_url = reverse_lazy("resources")
    template_name = "prodil/edit.html"


class ResourceDetailView(DetailView):
    model = Resource
    template_name = "prodil/detail.html"
