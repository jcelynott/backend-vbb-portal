from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from vbb_backend.users.models import Mentor
from vbb_backend.users.api.serializers.mentor import MentorSerializer
from rest_framework.permissions import AllowAny


class MentorCreateViewSet(CreateModelMixin, GenericViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = (AllowAny,)