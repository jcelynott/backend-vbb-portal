from dry_rest_permissions.generics import DRYPermissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from vbb_backend.users.api.serializers.student import StudentSerializer
from vbb_backend.program.models import Classroom, Program, School
from vbb_backend.users.models import Student
from vbb_backend.users.models import UserTypeEnum


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated, DRYPermissions]
    serializer_class = StudentSerializer
    lookup_field = "external_id"

    def get_queryset(self):
        queryset = self.queryset.filter(user__user_type=UserTypeEnum.STUDENT.value)
        user = self.request.user
        classroom = Classroom.objects.get(
            external_id=self.kwargs.get("classroom_external_id")
        )
        queryset = queryset.filter(classroom=classroom)
        if user.is_superuser:
            pass
        elif user.user_type in [UserTypeEnum.HEADMASTER.value]:
            queryset = queryset.filter(
                classroom__school__program__program_director=user
            )
        else:
            raise PermissionDenied()
        return queryset

    def get_classroom(self):
        return get_object_or_404(
            Classroom, external_id=self.kwargs.get("classroom_external_id")
        )

    def perform_create(self, serializer):
        serializer.save(classroom=self.get_classroom())
