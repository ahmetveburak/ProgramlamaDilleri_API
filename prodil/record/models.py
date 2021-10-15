from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
    BooleanField,
    CharField,
    FloatField,
    ImageField,
    IntegerField,
    ManyToManyField,
    Model,
    TextChoices,
    TextField,
    UniqueConstraint,
)
from django.db.models.fields import DateTimeField
from django.db.models.query_utils import Q
from django.utils.translation import gettext as _


class Author(Model):
    first_name = CharField(_("First Name"), max_length=50)
    last_name = CharField(_("Last Name"), max_length=50, blank=True)
    site = CharField(_("Web Site"), max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def full_name(self) -> str:
        return self.__str__()

    class Meta:
        ordering = ("last_name",)


class ProgrammingLanguage(Model):
    name = CharField(_("Programming Language Name"), max_length=50)
    enabled = BooleanField(_("Is Enabled?"))
    order = IntegerField(_("Order"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("order",)


class Resource(Model):
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

    name = CharField(_("Resource Name"), max_length=100, null=False)
    note = TextField(_("About"), max_length=300, default="")
    rating = FloatField(
        default=5.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )
    enabled = BooleanField(_("Is Enabled?"), default=False)
    authors = ManyToManyField(
        to=Author,
        related_name="resource_author",
        verbose_name=_("Authors of Resource"),
    )
    language = ManyToManyField(ProgrammingLanguage, verbose_name=_("Programming Language"))
    local = CharField(
        _("Language"),
        choices=Local.choices,
        default=Local.TURKISH,
        max_length=2,
    )
    level = CharField(
        _("Level"),
        choices=Level.choices,
        default=Level.BEGINNER,
        max_length=3,
    )
    content = CharField(
        _("Type of Resource"),
        choices=Content.choices,
        default=Content.DOCUMENT,
        max_length=2,
    )
    file_name = CharField(_("File Name"), max_length=100, blank=True)
    file_id = CharField(max_length=100, blank=True)
    url = CharField(_("Website"), max_length=100, blank=True)
    image = ImageField(
        _("Image"),
        upload_to="resource_imgs",
        default="not-found.jpg",
        blank=True,
    )
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.content} | {self.name}"

    def save(self, *args, **kwargs) -> None:
        # clear missfilled fields for non document choices
        if self.content != Resource.Content.DOCUMENT:
            self.file_name = ""
            self.file_id = ""

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ("name",)
        constraints = [
            UniqueConstraint(
                fields=("file_name",),
                condition=Q(content="DC"),
                name="unique_document_file_name",
            ),
        ]
