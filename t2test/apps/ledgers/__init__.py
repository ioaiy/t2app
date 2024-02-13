from django.apps import AppConfig


class LedgersAppConfig(AppConfig):
    name = 't2test.apps.ledgers'
    label = 'ledgers'
    verbose_name = 'Ledgers'

    def ready(self):
        import t2test.apps.ledgers.signals
