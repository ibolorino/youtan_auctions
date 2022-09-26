from rest_framework import viewsets

from youtan_auctions.auctions.models import Bank
from youtan_auctions.auctions.permissions import IsAadminOrReadOnly

from .serializers import BankSerializer


class BankViewSet(viewsets.ModelViewSet):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    permission_classes = [IsAadminOrReadOnly]
