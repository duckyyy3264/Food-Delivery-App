# Generated by Django 5.1 on 2024-08-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="is_selected",
            field=models.BooleanField(default=False),
        ),
    ]
