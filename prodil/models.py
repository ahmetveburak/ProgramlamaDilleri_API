from __future__ import annotations

from django.contrib import auth
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User as DUser
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
from multiselectfield import MultiSelectField

from .utils import ResourceChoices


class User(AbstractUser):
    def is_prodil_admin(self, user: User):
        if user.is_active and user.has_perm("prodil.prodil_admin"):
            return True
        return False


class Author(Model):
    first_name = CharField(verbose_name=_("First Name"), max_length=50)
    last_name = CharField(verbose_name=_("Last Name"), max_length=50, blank=True, default="")
    site = CharField(verbose_name=_("Web Site"), max_length=100, blank=True, null=True, default="")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ("last_name",)


class Category(Model):
    name = CharField(verbose_name=_("Programming Language Name"), max_length=40)
    enabled = BooleanField(verbose_name=_("Is Enabled?"))
    order = IntegerField(verbose_name=_("Order"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("order",)


class BotUser(Model):
    user_id = CharField(verbose_name=_("Telegram User ID"), max_length=100)
    first_name = CharField(verbose_name=_("First Name"), max_length=70, null=False)
    last_name = CharField(verbose_name=_("Last Name"), max_length=70, blank=True, default="")
    username = CharField(verbose_name=_("Username"), max_length=40, blank=True, default="")

    def __str__(self) -> str:
        return f"ID: {self.user_id} | Name: {self.first_name}"

    class Meta:
        ordering = ("user_id",)


class Resource(Model):
    name = CharField(verbose_name="Resource Name", max_length=100, null=False)
    note = CharField(verbose_name="About", max_length=300, null=True, blank=True)
    rating = FloatField(
        default=0.5,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )
    enabled = BooleanField(verbose_name="Is Enabled?", default=False)
    # https://docs.djangoproject.com/en/3.2/topics/db/models/#be-careful-with-related-name-and-related-query-name
    authors = ManyToManyField(
        to=Author,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        verbose_name="Authors of Resource",
    )
    language = ManyToManyField(to=Category, verbose_name="Programming Language")
    local = CharField(choices=ResourceChoices.get_local_choice(), max_length=2, verbose_name="Language")
    level = MultiSelectField(choices=ResourceChoices.get_level_choice(), max_length=11, verbose_name="Level")
    res_type = CharField(choices=ResourceChoices.get_resource_choice(), max_length=2, verbose_name="Type of Resource")
    file_name = CharField(max_length=100, blank=True, verbose_name="File Name")
    file_id = CharField(max_length=100, blank=True)
    url = CharField(max_length=100, blank=True, verbose_name="Website")
    image = ImageField(upload_to="resource_imgs", default="not-found.jpg", blank=True, verbose_name="Image")
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
