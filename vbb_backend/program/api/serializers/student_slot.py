from rest_framework import serializers

from vbb_backend.program.models import StudentSlotAssociation
from vbb_backend.users.api.serializers.student import StudentSerializer


class StudentSlotSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)
    student_obj = StudentSerializer(read_only=True, source="student")

    class Meta:
        model = StudentSlotAssociation
        exclude = ("deleted", "slot", "external_id")

    """
    Need to Check Authorisation to add user as well, user should be able to add students he has access to only*
    """