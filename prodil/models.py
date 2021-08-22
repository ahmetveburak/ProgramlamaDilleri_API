from django.contrib import auth
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
from django.db.models.query_utils import Q
from multiselectfield import MultiSelectField

from .utils import ResourceChoices


# will be replaced to AbstractUser model
def is_prodil_admin(User: DUser):
    if User.is_active and User.has_perm("prodil.prodil_admin"):
        return True
    return False


auth.models.User.add_to_class("is_prodil_admin", is_prodil_admin)


class Author(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50, blank=True, default="")
    site = CharField(max_length=100, blank=True, null=True, default="")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ("last_name",)


class Category(Model):
    name = CharField(max_length=40)
    enabled = BooleanField()
    order = IntegerField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("order",)


class BotUser(Model):
    user_id = CharField(max_length=100)
    first_name = CharField(max_length=70, null=False)
    last_name = CharField(max_length=70, blank=True, default="")
    username = CharField(max_length=40, blank=True, default="")

    def __str__(self) -> str:
        return f"ID: {self.user_id} | Name: {self.first_name}"

    class Meta:
        ordering = ("user_id",)


class Resource(Model):
    name = CharField(max_length=100, null=False)
    note = CharField(max_length=300, null=True, blank=True)
    rating = FloatField(
        default=0.5,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )
    enabled = BooleanField(default=False)
    # https://docs.djangoproject.com/en/3.2/topics/db/models/#be-careful-with-related-name-and-related-query-name
    authors = ManyToManyField(
        Author,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    language = ManyToManyField(Category)
    local = CharField(choices=ResourceChoices.LOCAL_CHOICE, max_length=2)
    level = MultiSelectField(choices=ResourceChoices.LEVEL_CHOICE, max_length=11)
    res_type = CharField(choices=ResourceChoices.RESOURCE_CHOICE, max_length=2)
    file_name = CharField(max_length=100, blank=True)
    file_id = CharField(max_length=100, blank=True)
    url = CharField(max_length=100, blank=True)
    image = ImageField(upload_to="resource_imgs", default="not-found.jpg", blank=True)

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
