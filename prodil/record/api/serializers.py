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
            "file_unique_id",
            "file_size",
            "url",
        )


class ResourceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = (
            "name",
            "file_name",
            "file_id",
            "file_unique_id",
            "file_size",
        )

    def create(self, validated_data):
        file_name = validated_data["file_name"]

        try:
            file = Resource.objects.get(file_name=file_name)
            file.name = validated_data["name"]
            file.file_id = validated_data["file_id"]
            file.file_unique_id = validated_data["file_unique_id"]
            file.file_size = validated_data["file_size"]

            file.save(update_fields=("name", "file_id", "file_unique_id", "file_size", "updated"))
            return file

        except Resource.DoesNotExist:
            return super().create(validated_data)


class ResourceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ("file_id", "file_size")


class CategorySerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(write_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "order")
