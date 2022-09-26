from django.db import models


class Bank(models.Model):
    name = models.CharField("Nome", max_length=255)
    cnpj = models.CharField("CNPJ", max_length=14, unique=True)

    class Meta:
        verbose_name = "Instituição Financeira"
        verbose_name_plural = "Instituições Financeiras"

    def __str__(self):
        return f"{self.name}"
