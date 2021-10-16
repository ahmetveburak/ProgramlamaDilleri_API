from django.db import models
from django.utils.translation import gettext as _


class BotUser(models.Model):
    user_id = models.CharField(_("Telegram User ID"), max_length=100, unique=True)
    first_name = models.CharField(_("First Name"), max_length=100, null=False)
    last_name = models.CharField(_("Last Name"), max_length=100, default="")
    username = models.CharField(_("Username"), max_length=100, default="")

    def __str__(self) -> str:
        return f"ID: {self.user_id} | Name: {self.first_name}"

    class Meta:
        verbose_name = _("botuser")
        verbose_name_plural = _("botusers")


class History(models.Model):
    user = models.ForeignKey(
        "botuser.BotUser",
        verbose_name="user history",
        on_delete=models.PROTECT,
    )
    created = models.DateTimeField(auto_now_add=True)
    resource = models.ManyToManyField("record.Resource", blank=True)

    class Meta:
        verbose_name = _("history")
        verbose_name_plural = _("histories")
