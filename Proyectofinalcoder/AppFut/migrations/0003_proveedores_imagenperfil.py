# Generated by Django 4.1.1 on 2022-10-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFut', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedores',
            name='imagenPerfil',
            field=models.ImageField(null=True, upload_to='perfiles'),
        ),
    ]
