# Generated by Django 5.1 on 2024-09-21 01:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("deliverer", "0012_alter_driverlicense_deliverer_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="operationinfo",
            old_name="operational_area",
            new_name="area",
        ),
        migrations.RenameField(
            model_name="operationinfo",
            old_name="operation_type",
            new_name="driver_type",
        ),
        migrations.RenameField(
            model_name="operationinfo",
            old_name="operational_time",
            new_name="time",
        ),
        migrations.AddField(
            model_name="operationinfo",
            name="hub",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]
