# Generated by Django 3.2.7 on 2024-08-04 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_initial'),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailinfo',
            name='restaurant_category',
        ),
        migrations.CreateModel(
            name='RestaurantCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_categories', to='food.dishcategory')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_categories', to='restaurant.restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='categories',
            field=models.ManyToManyField(related_name='restaurants', through='restaurant.RestaurantCategory', to='food.DishCategory'),
        ),
    ]
