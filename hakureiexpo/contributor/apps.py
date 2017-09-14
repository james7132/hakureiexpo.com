from django.apps import AppConfig


class ContributorConfig(AppConfig):
    name = 'contributor'

    def ready(self):
        import contributor.signals