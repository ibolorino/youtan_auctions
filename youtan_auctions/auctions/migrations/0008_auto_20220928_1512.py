# Generated by Django 3.2.15 on 2022-09-28 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20220928_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertyimages',
            options={'ordering': ['-id'], 'verbose_name': 'Imagem - Imóvel', 'verbose_name_plural': 'Imagens - Imóveis'},
        ),
        migrations.AlterModelOptions(
            name='vehicleimages',
            options={'ordering': ['-id'], 'verbose_name': 'Imagem - Veículo', 'verbose_name_plural': 'Imagens - Veículos'},
        ),
    ]
