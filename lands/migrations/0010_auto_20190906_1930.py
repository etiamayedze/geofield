# Generated by Django 2.2.4 on 2019-09-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0009_auto_20190906_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiqueproprio',
            name='dateDebutPossession',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='historiqueproprio',
            name='dateFinPossession',
            field=models.DateField(null=True),
        ),
    ]
