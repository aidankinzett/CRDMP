# Generated by Django 2.1 on 2018-10-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentalApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
