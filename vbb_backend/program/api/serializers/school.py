from rest_framework import serializers

from vbb_backend.program.models import School

from rest_framework.exceptions import ValidationError


class SchoolSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = School
        exclude = ("deleted", "program")
