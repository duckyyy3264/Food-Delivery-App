# Generated by Django 3.2.7 on 2024-07-19 10:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
        ('account', '0012_auto_20240719_0855'),
        ('order', '0005_auto_20240719_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpromotion',
            name='promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userpromotion_promotions', to='order.promotion'),
        ),
        migrations.AlterField(
            model_name='userpromotion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_promotions', to='account.userrelation'),
        ),
        migrations.CreateModel(
            name='RestaurantPromotion',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurantpromotion_promotions', to='order.promotion')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_promotions', to='restaurant.restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderPromotion',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='used_promotions', to='order.order')),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderpromotion_promotions', to='order.promotion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
