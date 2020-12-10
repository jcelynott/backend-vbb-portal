from rest_framework import serializers

from vbb_backend.program.models import Classroom

from rest_framework.exceptions import ValidationError


class ClassroomSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = Classroom
        exclude = ("deleted", "school", "external_id")
