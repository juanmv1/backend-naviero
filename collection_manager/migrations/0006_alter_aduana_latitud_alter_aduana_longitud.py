# Generated by Django 5.1.2 on 2024-10-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_manager', '0005_remove_historicalsector_region_remove_sector_region_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aduana',
            name='latitud',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='aduana',
            name='longitud',
            field=models.FloatField(null=True),
        ),
    ]