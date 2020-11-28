from django.contrib.auth import models
from rest_framework import serializers

from vbb_backend.program.models import Program


class ProgramSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = Program
        fields = "__all__"

    def validate(self, attrs):
        user = self.context["request"].user
        # Clean up Attributes based on what the user can access
        for attribute in Program.ACCESS_CONTROL:
            if attribute in attrs:
                if user.user_type not in Program.ACCESS_CONTROL[attribute]:
                    del attrs[attribute]
        return super().validate(attrs)