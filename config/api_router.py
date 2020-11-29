from django.conf import settings
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from vbb_backend.program.api.viewsets.program import ProgramViewSet
from vbb_backend.program.api.viewsets.school import SchoolViewSet
from vbb_backend.program.api.viewsets.classroom import ClassroomViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("program", ProgramViewSet)

program_nested_router = NestedSimpleRouter(router, r"program", lookup="program")


program_nested_router.register(r"school", SchoolViewSet)

school_nested_router = NestedSimpleRouter(
    program_nested_router, r"school", lookup="school"
)

school_nested_router.register(r"classroom", ClassroomViewSet)


app_name = "api"

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^", include(program_nested_router.urls)),
    url(r"^", include(school_nested_router.urls)),
]
