
from django.apps import AppConfig


class BusinessConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "electronic_store.business"

    def ready(self):
        import electronic_store.business.signals
