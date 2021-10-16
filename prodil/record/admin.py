from django.contrib import admin

from prodil.record.models import Author, Category, Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    filter_horizontal = ("author",)
    search_fields = ("local",)
    list_filter = ("local", "author")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
