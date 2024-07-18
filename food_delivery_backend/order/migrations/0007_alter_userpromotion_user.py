# Generated by Django 3.2.7 on 2024-07-19 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0006_auto_20240719_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpromotion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_promotions', to=settings.AUTH_USER_MODEL),
        ),
    ]
