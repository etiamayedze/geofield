# Generated by Django 2.2.4 on 2019-09-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0013_auto_20190914_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichier',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
    ]
