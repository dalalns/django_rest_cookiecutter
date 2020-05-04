from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class StudentsConfig(AppConfig):
    name = "d_react.students"
    verbose_name = _("Students")
    def ready(self):
        try:
            from . import signals
        except ImportError:
            pass
