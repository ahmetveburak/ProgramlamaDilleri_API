from django.apps import AppConfig


class RecordConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "prodil.record"

    def ready(self):
        import prodil.record.signals  # noqa
