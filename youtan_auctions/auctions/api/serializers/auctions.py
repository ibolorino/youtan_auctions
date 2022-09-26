from datetime import datetime

from rest_framework import serializers

from youtan_auctions.auctions.mixins import PrefetchedSerializer
from youtan_auctions.auctions.models import Auction

from .banks import BankSerializer


class AuctionSerializer(serializers.ModelSerializer, PrefetchedSerializer):
    class Meta:
        model = Auction
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["bank"] = BankSerializer(instance.bank).data
        return data

    def validate_date(self, value):
        if value <= datetime.now().date():
            raise serializers.ValidationError("Data do leilão deve ser maior que hoje.")
        return value
