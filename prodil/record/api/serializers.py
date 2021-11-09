from rest_framework import serializers

from prodil.record.models import Author, Category, Resource


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "full_name",
            "site",
        )


class ResourceSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)

    class Meta:
        model = Resource
        fields = (
            "name",
            "note",
            "rating",
            "enabled",
            "author",
            "category",
            "local",
            "level",
            "content",
            "file_name",
            "file_id",
            "file_size",
            "url",
        )


class ResourceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ("file_id", "file_size")


class CategorySerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(write_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "order")
