from django_filters import rest_framework as filters

from prodil.record.managers import Content, Level, Local
from prodil.record.models import Category, Resource


class ResourceFilter(filters.FilterSet):
    level = filters.ChoiceFilter(choices=Level.choices)
    local = filters.ChoiceFilter(choices=Local.choices)
    content = filters.ChoiceFilter(choices=Content.choices)
    category = filters.ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Resource
        fields = ("level", "local", "content", "category")
