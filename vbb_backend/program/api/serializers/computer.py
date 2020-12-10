from rest_framework import serializers

from vbb_backend.program.models import Computer

from rest_framework.exceptions import ValidationError


class ComputerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = Computer
        exclude = ("deleted", "program", "external_id")
