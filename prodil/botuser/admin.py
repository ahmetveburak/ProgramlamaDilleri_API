from django.contrib import admin

from prodil.botuser.models import BotUser


@admin.register(BotUser)
class BotUserAdmin:
    pass
