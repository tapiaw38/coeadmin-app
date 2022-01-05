"""Record app."""

# Django
from django.apps import AppConfig


class RecordAppConfig(AppConfig):
    """Record app config."""

    name = 'coeadmin.record'
    verbose_name = 'Records'

    '''
    def ready(self):
        """Load signals."""
        import coeadmin.record.signals  # noqa
        super().ready()
    '''