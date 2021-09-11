from django.contrib.auth import models
from django.db.models import fields
from prodil.models import Author, BotUser, ProgrammingLanguage, Resource
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("full_name",)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ("full_name",)


class ResourceSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Resource
        fields = (
            "name",
            "note",
            "rating",
            "enabled",
            "authors",
            "language",
            "local",
            "level",
            "res_type",
            "file_name",
            "file_id",
            "url",
            "image",
        )


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = (
            "user_id",
            "first_name",
            "last_name",
            "username",
        )
