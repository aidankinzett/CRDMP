# Generated by Django 2.1 on 2018-10-08 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RentalApp', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pickupStore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_pickup_store', to='RentalApp.Store'),
        ),
        migrations.AlterField(
            model_name='order',
            name='returnStore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='return_store', to='RentalApp.Store'),
        ),
    ]
