from rest_framework import serializers

from youtan_auctions.auctions.models import Auction


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = [
            "id",
            "name",
            "date",
            "address",
            "city",
            "state",
            "zip_code",
            "bank",
        ]
        read_only_fields = [
            "id",
        ]
