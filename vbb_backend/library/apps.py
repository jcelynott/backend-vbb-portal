from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LibraryConfig(AppConfig):
    name = "vbb_backend.library"
    verbose_name = _("Library")

    def ready(self):
        try:
            import vbb_backend.library.signals  # noqa F401
        except ImportError:
            pass
