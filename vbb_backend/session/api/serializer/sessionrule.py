from rest_framework import serializers

from vbb_backend.session.models import SessionRule
from vbb_backend.users.api.serializers.user import UserBareMinimumSerializer


class SessionRuleSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)
    mentor = UserBareMinimumSerializer()

    class Meta:
        model = SessionRule
        exclude = ("deleted", "slot", "external_id")
