# Generated by Django 4.0.4 on 2022-05-28 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0019_alter_messagemodel_body'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MessageModel',
        ),
    ]
