from rest_framework import serializers

from youtan_auctions.auctions.api.validators import validate_bid
from youtan_auctions.auctions.mixins import PrefetchedSerializer
from youtan_auctions.auctions.models import (
    Properties_Bids,
    Property,
    Vehicle,
    Vehicles_Bids,
)
from youtan_auctions.users.models import User

from .auctions import AuctionSerializer


class Properties_BidsSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
        slug_field="username",
    )

    class Meta:
        model = Properties_Bids
        fields = "__all__"

    def validate(self, data):
        return validate_bid(data, "property")


class PropertySerializer(serializers.ModelSerializer, PrefetchedSerializer):
    bids = Properties_BidsSerializer(
        many=True, source="properties_bids_set", read_only=True
    )

    class Meta:
        model = Property
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["auction"] = AuctionSerializer(instance.auction).data
        return data


class Vehicles_BidsSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
        slug_field="username",
    )

    class Meta:
        model = Vehicles_Bids
        fields = "__all__"

    def validate(self, data):
        return validate_bid(data, "vehicle")


class VehicleSerializer(serializers.ModelSerializer, PrefetchedSerializer):
    bids = Vehicles_BidsSerializer(
        many=True, source="vehicles_bids_set", read_only=True
    )

    class Meta:
        model = Vehicle
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["auction"] = AuctionSerializer(instance.auction).data
        return data
