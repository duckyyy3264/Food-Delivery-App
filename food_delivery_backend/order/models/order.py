import uuid
import decimal

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from order.models import RestaurantCart, Delivery, DeliveryRequest
from deliverer.models import Deliverer
from utils.objects import Point, Distance

class Order(models.Model):
    class Meta:
        ordering = ['-created_at']
        
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("CANCELLED", "Cancelled"),
        ("COMPLETED", "Completed"),
        ("PENDING", "Pending")
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    cart = models.OneToOneField("order.RestaurantCart", related_name="order", on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    promotion = models.ForeignKey("order.Promotion", null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")
    rating = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def total(self):
        return float(self.cart.total_price) + float(self.delivery_fee()) - float(self.discount)
    
    def delivery_address(self):
        user = self.cart.user  
        selected_location = user.locations.filter(is_selected=True).first()
        return selected_location

    def delivery_fee(self):
        delivery_address = self.delivery_address()
        if not self.cart or not delivery_address:
            return decimal.Decimal('0.00')

        restaurant_coordinate = Point(
            float(self.cart.restaurant.basic_info.latitude),
            float(self.cart.restaurant.basic_info.longitude)
        )
        user_coordinate = Point(
            float(delivery_address.latitude),
            float(delivery_address.longitude),

        )
        
        distance = Distance.haversine(
            restaurant_coordinate,
            user_coordinate
        )

        base_fee = 2.00  
        fee_per_km = 0.50  

        delivery_fee = base_fee + (fee_per_km * distance)
        return decimal.Decimal(delivery_fee).quantize(decimal.Decimal('0.00'))
    
    def create_delivery_and_request(self, create_delivery=False):
        restaurant = self.cart.restaurant
        user = self.cart.user
        delivery_address = self.delivery_address()

        if not delivery_address:
            return

        delivery, created_delivery = Delivery.objects.get_or_create(
            order=self,
            user=user,
            restaurant=restaurant,
            defaults={
                'pickup_location': restaurant.basic_info.street_address,
                'pickup_latitude': restaurant.basic_info.latitude,
                'pickup_longitude': restaurant.basic_info.longitude,
                'dropoff_location': delivery_address.address,
                'dropoff_latitude': delivery_address.latitude,
                'dropoff_longitude': delivery_address.longitude,
            }
        )
        nearest_deliverer = DeliveryRequest._find_nearest_deliverer(delivery, Deliverer.objects.filter(is_active=True, is_occupied=False))

        if nearest_deliverer:
            delivery_request, created_request = DeliveryRequest.objects.get_or_create(
                deliverer=nearest_deliverer,
                delivery=delivery,
                defaults={
                    'status': 'PENDING'
                }
            )
        print(nearest_deliverer, pretty=True)

        return delivery, nearest_deliverer


    def __str__(self):
        return f"Order for {self.cart} with total {self.total()}"


# @receiver(post_save, sender='order.Order')
# def broadcast_to_deliverers(sender, instance, **kwargs):
#     if instance.status == 'ACTIVE':
#         create_delivery_and_requests(instance, create_delivery=True)


@receiver(post_save, sender='order.Order')
def broadcast_to_deliverers(sender, instance, **kwargs):
    instance.cart.is_created_order = True