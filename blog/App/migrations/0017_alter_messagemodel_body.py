# Generated by Django 4.0.4 on 2022-05-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0016_threadmodel_messagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='body',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
