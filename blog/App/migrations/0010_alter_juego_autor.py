# Generated by Django 4.0.4 on 2022-05-26 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0009_alter_avatar_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
