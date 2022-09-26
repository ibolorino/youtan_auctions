from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuctionsConfig(AppConfig):
    name = "youtan_auctions.auctions"
    verbose_name = _("Auctions")

    def ready(self):
        try:
            import youtan_auctions.auctions.signals  # noqa F401
        except ImportError:
            pass
