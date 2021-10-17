from rest_framework import serializers

from prodil.record.models import Resource


class ResourceSerializer(serializers.ModelSerializer):
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
            "url",
        )
