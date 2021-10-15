from django.contrib import admin

from prodil.record.models import Author, ProgrammingLanguage, Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    filter_horizontal = ("authors", "language")
    search_fields = ("language",)
    list_filter = ("language", "authors")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
    )


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    pass
