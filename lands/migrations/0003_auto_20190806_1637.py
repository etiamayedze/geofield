# Generated by Django 2.2.2 on 2019-08-06 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0002_proprietaire_date_naiss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proprietaire',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
