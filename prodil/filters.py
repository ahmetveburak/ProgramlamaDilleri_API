from django.db.models import fields
from django_filters import CharFilter, FilterSet, TypedMultipleChoiceFilter

from prodil.models import Resource


class ResourceFilter(FilterSet):
    level = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Resource
        fields = (
            "language",
            "local",
            "level",
            "res_type",
        )


# class ResourceFilter(FilterSet):
#     class Meta:
#         model = Resource
#         fields = {
#             "language": ["exact"],
#             "local": ["exact"],
#             "level": ["icontains"],
#             "res_type": ["exact"],
#         }
