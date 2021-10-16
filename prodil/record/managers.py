from django.db.models import TextChoices
from django.utils.translation import gettext as _


class Level(TextChoices):
    BEGINNER = "BGN", _("Beginner")
    EXPERIENCED = "EXP", _("Experienced")
    PROFESSIONAL = "PRO", _("Professional")


class Local(TextChoices):
    ENGLISH = "EN", _("English")
    TURKISH = "TR", _("Turkish")


class Content(TextChoices):
    BOOK = "BK", _("Book")
    DOCUMENT = "DC", _("Document")
    LINK = "LN", _("Link")
