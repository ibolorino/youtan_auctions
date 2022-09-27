from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from youtan_auctions.auctions.api.views import (
    AuctionViewSet,
    BankViewSet,
    PropertyViewSet,
)
from youtan_auctions.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("auctions", AuctionViewSet, basename="auctions")
router.register("banks", BankViewSet, basename="banks")
router.register("properties", PropertyViewSet, basename="properties")


app_name = "api"
urlpatterns = router.urls
