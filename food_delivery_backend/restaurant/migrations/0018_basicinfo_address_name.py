# Generated by Django 5.1 on 2024-10-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0017_alter_basicinfo_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="basicinfo",
            name="address_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
