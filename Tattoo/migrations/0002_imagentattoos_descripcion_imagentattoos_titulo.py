# Generated by Django 4.2.2 on 2023-08-05 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tattoo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagentattoos',
            name='descripcion',
            field=models.CharField(default='Descripción predeterminada', max_length=100),
        ),
        migrations.AddField(
            model_name='imagentattoos',
            name='titulo',
            field=models.CharField(default='titulo predeterminada', max_length=50),
        ),
    ]