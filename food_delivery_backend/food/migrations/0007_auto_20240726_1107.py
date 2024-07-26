# Generated by Django 3.2.7 on 2024-07-26 04:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20240726_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishadditionaloption',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dishcategory',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dishlike',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dishsizeoption',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
