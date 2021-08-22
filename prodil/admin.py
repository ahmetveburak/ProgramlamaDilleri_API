from django.contrib import admin

from prodil.models import Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    filter_horizontal = ("authors", "language")
    search_fields = ("language",)
    list_filter = ("language", "authors")
