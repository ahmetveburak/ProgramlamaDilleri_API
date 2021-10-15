from django.db.models import CharField, Model
from django.utils.translation import gettext as _


class BotUser(Model):
    user_id = CharField(_("Telegram User ID"), max_length=100)
    first_name = CharField(_("First Name"), max_length=70, null=False)
    last_name = CharField(_("Last Name"), max_length=70, blank=True, default="")
    username = CharField(_("Username"), max_length=40, blank=True, default="")

    def __str__(self) -> str:
        return f"ID: {self.user_id} | Name: {self.first_name}"

    class Meta:
        ordering = ("user_id",)
