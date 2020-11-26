from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

# from vbb_backend.users.api.viewsets.mentor import MentorCreateViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("register", MentorCreateViewSet)

app_name = "api"
urlpatterns = router.urls
