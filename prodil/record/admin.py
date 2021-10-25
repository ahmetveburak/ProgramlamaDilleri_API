from django.contrib import admin

from prodil.record.models import Author, Category, Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    filter_horizontal = ("author", "category")
    search_fields = (
        "name",
        "file_name",
        "level",
    )
    list_display = (
        "name",
        "categories",
        "local",
        "level",
        "content",
        "rating",
        "enabled",
    )
    list_filter = ("local", "level", "content", "category")

    fieldsets = (
        (
            "Base",
            {"fields": ("name", "note", "rating", "enabled")},
        ),
        (
            "Information",
            {"fields": ("author", "category", "level", "local", "content")},
        ),
        (
            "Media",
            {"fields": ("url", "image")},
        ),
        (
            "File Info",
            {"fields": ("file_name",)},
        ),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "site")
    list_filter = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "enabled", "order")
    list_filter = ("enabled",)
