from rest_framework import serializers

from youtan_auctions.auctions.mixins import PrefetchedSerializer
from youtan_auctions.auctions.models import Properties_Bids, Property

from .auctions import AuctionSerializer


class Properties_BidsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Properties_Bids
        exclude = ["property"]


class PropertySerializer(serializers.ModelSerializer, PrefetchedSerializer):
    bids = Properties_BidsSerializer(many=True, source="properties_bids_set")

    class Meta:
        model = Property
        fields = "__all__"
        read_only_fields = [
            "bids",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["auction"] = AuctionSerializer(instance.auction).data
        # data["bids"] = Properties_BidsSerializer(instance.bids).data
        return data
