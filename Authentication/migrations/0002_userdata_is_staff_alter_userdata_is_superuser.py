# Generated by Django 4.2.4 on 2023-08-06 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
