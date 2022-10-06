from django.db import models
from django.core.validators import MinLengthValidator

from youtan_auctions.auctions.utils import get_image_path
from youtan_auctions.users.models import User

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
    area = models.FloatField("Área (m²)")
    debtis = models.BooleanField("Há débitos")
    observation = models.TextField("Observações")
    address = models.CharField("Endereço", max_length=255)
    city = models.CharField("Cidade", max_length=255)
    state = models.CharField("Estado", max_length=255)
    zip_code = models.CharField("CEP", max_length=15)
    bids = models.ManyToManyField(
        User, verbose_name="Lances", through="Properties_Bids", blank=True
    )
    minimum_increment = models.IntegerField("Incremento Mínimo")

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"

    def __str__(self):
        return f"{self.name}"


class Properties_Bids(models.Model):
    user = models.ForeignKey(User, verbose_name="Cliente", on_delete=models.DO_NOTHING)
    property = models.ForeignKey(
        Property, verbose_name="Imóvel", on_delete=models.CASCADE
    )
    date = models.DateTimeField("Data/Hora", auto_now=False, auto_now_add=True)
    value = models.DecimalField("Lance", max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = "Lance - Imóvel"
        verbose_name_plural = "Lances - Imóveis"
        ordering = ["-id"]


class PropertyImages(models.Model):
    property = models.ForeignKey(
        Property, verbose_name="Imóvel", on_delete=models.CASCADE
    )
    image = models.ImageField("Imagem", upload_to=get_image_path, max_length=None)

    class Meta:
        verbose_name = "Imagem - Imóvel"
        verbose_name_plural = "Imagens - Imóveis"
        ordering = ["-id"]


class Vehicle(models.Model):
    auction = models.ForeignKey(
        Auction, verbose_name="Leilão", on_delete=models.CASCADE
    )
    name = models.CharField("Nome", max_length=255)
    vehicle_type = models.CharField("Tipo de veículo", max_length=255)
    initial_bid = models.DecimalField("Lance inicial", max_digits=20, decimal_places=2)
    origin = models.CharField("Origem", max_length=255)
    mileage = models.IntegerField("Quilometragem")
    plate = models.CharField("Placa", max_length=7, validators=[MinLengthValidator(7)])
    transmission = models.CharField("Câmbio", max_length=255)
    brand = models.CharField("Marca", max_length=255)
    model = models.CharField("Modelo", max_length=255)
    year = models.IntegerField("Ano")
    fuel = models.CharField("Combustível", max_length=255)
    observation = models.TextField("Observações")
    bids = models.ManyToManyField(
        User, verbose_name="Lances", through="Vehicles_Bids", blank=True
    )
    minimum_increment = models.IntegerField("Incremento Mínimo")

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"

    def __str__(self):
        return f"{self.name}"


class Vehicles_Bids(models.Model):
    user = models.ForeignKey(User, verbose_name="Cliente", on_delete=models.DO_NOTHING)
    vehicle = models.ForeignKey(
        Vehicle, verbose_name="Veículo", on_delete=models.CASCADE
    )
    date = models.DateTimeField("Data/Hora", auto_now=False, auto_now_add=True)
    value = models.DecimalField("Lance", max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = "Lance - Veículo"
        verbose_name_plural = "Lances - Veículos"
        ordering = ["-id"]


class VehicleImages(models.Model):
    vehicle = models.ForeignKey(
        Vehicle, verbose_name="Veículo", on_delete=models.CASCADE
    )
    image = models.ImageField("Imagem", upload_to=get_image_path, max_length=None)

    class Meta:
        verbose_name = "Imagem - Veículo"
        verbose_name_plural = "Imagens - Veículos"
        ordering = ["-id"]
