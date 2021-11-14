from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
    BooleanField,
    CharField,
    FloatField,
    ImageField,
    IntegerField,
    ManyToManyField,
    Model,
    PositiveIntegerField,
    Q,
    TextField,
    UniqueConstraint,
)
from django.db.models.fields import DateTimeField
from django.utils.translation import gettext as _
from uuslug import uuslug

from prodil.record.managers import Content, Level, Local


class Author(Model):
    first_name = CharField(_("First Name"), max_length=50)
    last_name = CharField(_("Last Name"), max_length=50, blank=True)
    site = CharField(_("Web Site"), max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def full_name(self) -> str:
        return self.__str__()

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")


class Category(Model):
    name = CharField(_("Category Name"), max_length=50)
    enabled = BooleanField(_("Is Enabled?"), default=True)
    order = IntegerField(_("Order"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class Resource(Model):
    name = CharField(_("Resource Name"), max_length=100, null=False)
    slug = CharField(_("Slug"), max_length=200)
    note = TextField(_("Note"), max_length=300, default="", blank=True)
    rating = FloatField(
        _("Rating"),
        default=5.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )
    enabled = BooleanField(_("Is Enabled?"), default=True)
    author = ManyToManyField(
        to=Author,
        related_name="resource_authors",
        verbose_name=_("Authors"),
    )
    category = ManyToManyField(Category, verbose_name=_("Category"))
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
    file_name = CharField(_("File Name"), max_length=255, null=True, blank=True)
    file_id = CharField(_("File ID"), max_length=100, default="", null=True, blank=True)
    file_size = PositiveIntegerField(_("File Size"), null=True, blank=True)
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

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = uuslug(self.name, instance=self)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("resource")
        verbose_name_plural = _("resources")
        constraints = [
            UniqueConstraint(
                fields=("file_name",),
                condition=Q(content=Content.DOCUMENT),
                name="unique_document_file_name",
            ),
        ]

    def categories(self):
        return ", ".join([i.name for i in self.category.all()])
