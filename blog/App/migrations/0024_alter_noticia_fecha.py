# Generated by Django 4.0.4 on 2022-05-29 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0023_remove_threadmodel_receiver_remove_threadmodel_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
