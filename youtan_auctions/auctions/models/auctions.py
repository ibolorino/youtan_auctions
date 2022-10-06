from django.db import models

from .banks import Bank


class Auction(models.Model):
    name = models.CharField("Nome", max_length=255)
    date = models.DateField("Data", auto_now=False, auto_now_add=False)
    address = models.CharField("Endereço", max_length=255)
    city = models.CharField("Cidade", max_length=255)
    state = models.CharField("Estado", max_length=255)
    zip_code = models.CharField("CEP", max_length=15)
    bank = models.ForeignKey(
        Bank, verbose_name="Instituição Financeira", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Leilão"
        verbose_name_plural = "Leilões"

    def __str__(self):
        return f"{self.name}"
