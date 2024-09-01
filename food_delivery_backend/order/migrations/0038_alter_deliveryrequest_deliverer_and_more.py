# Generated by Django 5.1 on 2024-09-05 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("deliverer", "0006_rename_is_busy_deliverer_is_occupied"),
        ("order", "0037_alter_delivery_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deliveryrequest",
            name="deliverer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="_delivery_requests",
                to="deliverer.deliverer",
            ),
        ),
        migrations.AlterField(
            model_name="deliveryrequest",
            name="delivery",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="_delivery_requests",
                to="order.delivery",
            ),
        ),
    ]
