# Generated by Django 4.0.4 on 2022-05-26 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_juego_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='imagen',
        ),
    ]
