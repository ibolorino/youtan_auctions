# Generated by Django 3.2.15 on 2022-10-06 20:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20220928_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.bank', verbose_name='Instituição Financeira'),
        ),
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.FloatField(verbose_name='Área (m²)'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='plate',
            field=models.CharField(max_length=7, validators=[django.core.validators.MinLengthValidator(7)], verbose_name='Placa'),
        ),
    ]
