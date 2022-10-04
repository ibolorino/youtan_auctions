from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

from youtan_auctions.auctions.models import (
    Auction,
    Bank,
    Property,
    PropertyImages,
    Vehicle,
    VehicleImages,
)
from youtan_auctions.auctions.permissions import IsAdminOrReadOnly

from .actions import BidActions, ImageActions
from .serializers import (
    AuctionSerializer,
    BankSerializer,
    Properties_BidsSerializer,
    PropertyImagesSerializer,
    PropertySerializer,
    VehicleImagesSerializer,
    Vehicles_BidsSerializer,
    VehicleSerializer,
)


class BankViewSet(viewsets.ModelViewSet):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class AuctionViewSet(viewsets.ModelViewSet):
    serializer_class = AuctionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Auction.objects.filter(date__gt=datetime.now().date())
        if queryset:
            queryset = self.get_serializer_class().select_related_queryset(
                queryset, ["bank"]
            )
        return queryset.order_by("date")


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        auction_id = self.request.query_params.get("auction_id")
        queryset = Property.objects.all()
        if queryset:
            queryset = self.get_serializer_class().select_related_queryset(
                queryset, ["auction"]
            )
        if auction_id:
            queryset = queryset.filter(auction__id=auction_id)
        return queryset


class PropertyImagesViewSet(ImageActions, viewsets.ModelViewSet):
    serializer_class = PropertyImagesSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = PropertyImages.objects.all()


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        auction_id = self.request.query_params.get("auction_id")
        queryset = Vehicle.objects.all()
        if queryset:
            queryset = self.get_serializer_class().select_related_queryset(
                queryset, ["auction"]
            )
        if auction_id:
            queryset = queryset.filter(auction__id=auction_id)
        return queryset


class VehicleImagesViewSet(ImageActions, viewsets.ModelViewSet):
    serializer_class = VehicleImagesSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = VehicleImages.objects.all()


class BidViewSet(BidActions, CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "property":
            return Properties_BidsSerializer
        elif self.action == "vehicle":
            return Vehicles_BidsSerializer
