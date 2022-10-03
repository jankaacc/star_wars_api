from rest_framework import serializers

from starwars.people.models import PeopleDataset


class PeopleDatasetSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%d %b %Y %H:%M:%S", read_only=True
    )
    updated_at = serializers.DateTimeField(
        format="%d %b %Y %H:%M:%S", read_only=True
    )

    class Meta:
        model = PeopleDataset
        fields = "__all__"
