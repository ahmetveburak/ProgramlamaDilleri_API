from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
    BooleanField,
    CharField,
    FloatField,
    ImageField,
    IntegerField,
    ManyToManyField,
    Model,
    UniqueConstraint,
)
from django.db.models.fields import DateTimeField
from django.db.models.query_utils import Q
from django.utils.translation import gettext as _

from prodil.utils import ResourceChoices


class Author(Model):
    first_name = CharField(_("First Name"), max_length=50)
    last_name = CharField(_("Last Name"), max_length=50, blank=True, default="")
    site = CharField(_("Web Site"), max_length=100, blank=True, null=True, default="")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def full_name(self) -> str:
        return self.__str__()

    class Meta:
        ordering = ("last_name",)


class ProgrammingLanguage(Model):
    name = CharField(_("Programming Language Name"), max_length=40)
    enabled = BooleanField(_("Is Enabled?"))
    order = IntegerField(_("Order"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("order",)


class BotUser(Model):
    user_id = CharField(_("Telegram User ID"), max_length=100)
    first_name = CharField(_("First Name"), max_length=70, null=False)
    last_name = CharField(_("Last Name"), max_length=70, blank=True, default="")
    username = CharField(_("Username"), max_length=40, blank=True, default="")

    def __str__(self) -> str:
        return f"ID: {self.user_id} | Name: {self.first_name}"

    class Meta:
        ordering = ("user_id",)


class Resource(Model):
    name = CharField(_("Resource Name"), max_length=100, null=False)
    note = CharField(_("About"), max_length=300, null=True, blank=True)
    rating = FloatField(
        default=0.5,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )
    enabled = BooleanField(_("Is Enabled?"), default=False)
    # https://docs.djangoproject.com/en/3.2/topics/db/models/#be-careful-with-related-name-and-related-query-name
    authors = ManyToManyField(
        to=Author,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        verbose_name="Authors of Resource",
    )
    language = ManyToManyField(verbose_name=_("Programming Language"), to=ProgrammingLanguage)
    local = CharField(_("Language"), choices=ResourceChoices.get_local_choice(), max_length=2)
    level = CharField(_("Level"), choices=ResourceChoices.get_level_choice(), max_length=3)
    res_type = CharField(_("Type of Resource"), choices=ResourceChoices.get_resource_choice(), max_length=2)
    file_name = CharField(_("File Name"), max_length=100, blank=True)
    file_id = CharField(max_length=100, blank=True)
    url = CharField(_("Website"), max_length=100, blank=True)
    image = ImageField(_("Image"), upload_to="resource_imgs", default="not-found.jpg", blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.res_type} | {self.name}"

    def save(self, *args, **kwargs) -> None:
        # clear missfilled fields for non document choices
        if self.res_type != ResourceChoices.DOCUMENT:
            self.file_name = ""
            self.file_id = ""

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ("name",)
        constraints = [
            UniqueConstraint(
                fields=("file_name",),
                condition=Q(res_type=ResourceChoices.DOCUMENT),
                name="unique_document_file_name",
            ),
        ]
