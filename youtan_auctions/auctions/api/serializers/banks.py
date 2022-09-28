import re

from rest_framework import serializers

from youtan_auctions.auctions.models import Bank


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"

    # O correto aqui seria utilizar um script para verificar se o CNPJ é válido, porém,
    # optei por fazer somente a validação de tamanho para facilitar o cadastro
    def validate_cnpj(self, value):
        pattern = re.compile("[^0-9]")
        cnpj = pattern.sub("", str(value))

        if len(cnpj) != 14:
            raise serializers.ValidationError("CNPJ deve ter 14 dígitos")
        return value
