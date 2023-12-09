from django.apps import AppConfig


class SimpeappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simpeapp'

    def ready(self):
        from . import signals

