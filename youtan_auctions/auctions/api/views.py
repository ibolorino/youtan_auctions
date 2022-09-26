from rest_framework import viewsets

from youtan_auctions.auctions.models import Auction, Bank
from youtan_auctions.auctions.permissions import IsAadminOrReadOnly

from .serializers import AuctionSerializer, BankSerializer


class BankViewSet(viewsets.ModelViewSet):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    permission_classes = [IsAadminOrReadOnly]


class AuctionViewSet(viewsets.ModelViewSet):
    serializer_class = AuctionSerializer
    permission_classes = [IsAadminOrReadOnly]

    def get_queryset(self):
        queryset = Auction.objects.all()
        if queryset:
            queryset = self.get_serializer_class().select_related_queryset(
                queryset, ["bank"]
            )
        return queryset
