from django.db import models

from .auctions import Auction


class Property(models.Model):
    auction = models.ForeignKey(
        Auction, verbose_name="Leilão", on_delete=models.CASCADE
    )
    name = models.CharField("Nome", max_length=255)
    property_type = models.CharField("Tipo de imóvel", max_length=255)
    initial_bid = models.DecimalField("Lance inicial", max_digits=20, decimal_places=2)
    origin = models.CharField("Origem", max_length=255)
    status = models.CharField("Situação", max_length=255)
    area = models.FloatField("Área")
    debtis = models.BooleanField("Há débitos")
    observation = models.TextField("Observações")
    address = models.CharField("Endereço", max_length=255)
    city = models.CharField("Cidade", max_length=255)
    state = models.CharField("Estado", max_length=255)
    zip_code = models.CharField("CEP", max_length=15)

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"

    def __str__(self):
        return f"{self.name}"


class Vehicle(models.Model):
    auction = models.ForeignKey(
        Auction, verbose_name="Leilão", on_delete=models.CASCADE
    )
    name = models.CharField("Nome", max_length=255)
    vehicle_type = models.CharField("Tipo de veículo", max_length=255)
    initial_bid = models.DecimalField("Lance inicial", max_digits=20, decimal_places=2)
    origin = models.CharField("Origem", max_length=255)
    mileage = models.IntegerField("Quilometragem")
    plate = models.CharField("Placa", max_length=7)
    transmission = models.CharField("Câmbio", max_length=255)
    brand = models.CharField("Marca", max_length=255)
    model = models.CharField("Modelo", max_length=255)
    year = models.IntegerField("Ano")
    fuel = models.CharField("Combustível", max_length=255)
    observation = models.TextField("Observações")

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"

    def __str__(self):
        return f"{self.name}"
