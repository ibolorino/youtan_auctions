from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated

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
        queryset = Auction.objects.all()
        if queryset:
            queryset = self.get_serializer_class().select_related_queryset(
                queryset, ["bank"]
            )
        return queryset


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Property.objects.all()
        if queryset:
            queryset = self.get_serializer_class().select_related_queryset(
                queryset, ["auction"]
            )
        return queryset


class PropertyImagesViewSet(ImageActions, viewsets.ModelViewSet):
    serializer_class = PropertyImagesSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = PropertyImages.objects.all()


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        if queryset:
            queryset = self.get_serializer_class().select_related_queryset(
                queryset, ["auction"]
            )
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
