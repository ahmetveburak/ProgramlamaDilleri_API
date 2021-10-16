from django.contrib import admin

from prodil.auth.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
