from rest_framework import serializers

from youtan_auctions.auctions.models import Bank


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            "id",
            "name",
            "cnpj",
        ]
        read_only_fields = [
            "id",
        ]
