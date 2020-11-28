from rest_framework import serializers

from vbb_backend.users.models import User


class UserBareMinimumSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "id", "external_id")
