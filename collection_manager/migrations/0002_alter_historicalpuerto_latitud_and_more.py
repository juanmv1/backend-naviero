# Generated by Django 5.1.2 on 2024-10-13 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpuerto',
            name='latitud',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='historicalpuerto',
            name='longitud',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='historicalpuerto',
            name='zona_geografica',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='puerto',
            name='latitud',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='puerto',
            name='longitud',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='puerto',
            name='zona_geografica',
            field=models.CharField(max_length=255, null=True),
        ),
    ]