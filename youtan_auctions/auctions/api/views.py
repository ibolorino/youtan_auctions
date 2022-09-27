from rest_framework import viewsets

from youtan_auctions.auctions.models import Auction, Bank, Property
from youtan_auctions.auctions.permissions import CustomPermission

from .actions import PropertyActions
from .serializers import AuctionSerializer, BankSerializer, PropertySerializer


class BankViewSet(viewsets.ModelViewSet):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    permission_classes = [CustomPermission]


class AuctionViewSet(viewsets.ModelViewSet):
    serializer_class = AuctionSerializer
    permission_classes = [CustomPermission]

    def get_queryset(self):
        queryset = Auction.objects.all()
        if queryset:
            queryset = self.get_serializer_class().select_related_queryset(
                queryset, ["bank"]
            )
        return queryset


class PropertyViewSet(PropertyActions, viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    permission_classes = [CustomPermission]
    allowed_actions = ["bid"]

    def get_queryset(self):
        queryset = Property.objects.all()
        if queryset:
            queryset = self.get_serializer_class().select_related_queryset(
                queryset, ["auction"]
            )
        return queryset
