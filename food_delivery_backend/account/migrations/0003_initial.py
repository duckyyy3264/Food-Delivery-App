# Generated by Django 3.2.7 on 2024-07-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('review', '0001_initial'),
        ('order', '0001_initial'),
        ('notification', '0001_initial'),
        ('restaurant', '0001_initial'),
        ('social', '0001_initial'),
        ('deliverer', '0001_initial'),
        ('food', '0001_initial'),
        ('account', '0002_user_liked_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='liked_deliverer_reviews',
            field=models.ManyToManyField(related_name='liked_by_users', through='review.DelivererReviewLike', to='review.DelivererReview'),
        ),
        migrations.AddField(
            model_name='user',
            name='liked_delivery_reviews',
            field=models.ManyToManyField(related_name='liked_by_users', through='review.DeliveryReviewLike', to='review.DeliveryReview'),
        ),
        migrations.AddField(
            model_name='user',
            name='liked_dish_reviews',
            field=models.ManyToManyField(related_name='liked_by_users', through='review.DishReviewLike', to='review.DishReview'),
        ),
        migrations.AddField(
            model_name='user',
            name='liked_dishes',
            field=models.ManyToManyField(related_name='liked_by_users', through='food.DishLike', to='food.Dish'),
        ),
        migrations.AddField(
            model_name='user',
            name='liked_posts',
            field=models.ManyToManyField(related_name='liked_by_users', through='social.PostLike', to='social.Post'),
        ),
        migrations.AddField(
            model_name='user',
            name='liked_restaurant_reviews',
            field=models.ManyToManyField(related_name='liked_by_users', through='review.RestaurantReviewLike', to='review.RestaurantReview'),
        ),
        migrations.AddField(
            model_name='user',
            name='notifications',
            field=models.ManyToManyField(related_name='owned_by_users', through='notification.UserNotification', to='notification.Notification'),
        ),
        migrations.AddField(
            model_name='user',
            name='promotions',
            field=models.ManyToManyField(related_name='owned_by_users', through='order.UserPromotion', to='order.Promotion'),
        ),
        migrations.AddField(
            model_name='user',
            name='rated_deliverers',
            field=models.ManyToManyField(related_name='rated_by_users', through='review.DelivererReview', to='deliverer.Deliverer'),
        ),
        migrations.AddField(
            model_name='user',
            name='rated_deliveries',
            field=models.ManyToManyField(related_name='rated_by_users', through='review.DeliveryReview', to='order.Delivery'),
        ),
        migrations.AddField(
            model_name='user',
            name='rated_dishes',
            field=models.ManyToManyField(related_name='rated_by_users', through='review.DishReview', to='food.Dish'),
        ),
        migrations.AddField(
            model_name='user',
            name='rated_restaurants',
            field=models.ManyToManyField(related_name='rated_by_users', through='review.RestaurantReview', to='restaurant.Restaurant'),
        ),
    ]
