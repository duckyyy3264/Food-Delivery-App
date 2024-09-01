from rest_framework import serializers
from order.models import (
    Delivery,
    DeliveryRequest,
)

from account.serializers.basic_user import BasicUserSerializer
from restaurant.serializers.basic_restaurant import BasicRestaurantSerializer
from order.serializers.order import OrderSerializer

from utils.serializers import CustomRelatedModelSerializer
from utils.function import camel_to_snake


class DeliverySerializer(CustomRelatedModelSerializer):
    order = OrderSerializer(read_only=True)
    user = BasicUserSerializer(read_only=True)
    restaurant = BasicRestaurantSerializer(read_only=True)

    class Meta:
        model = Delivery
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']


class DeliveryRequestSerializer(serializers.ModelSerializer):
    delivery = serializers.SerializerMethodField()
    user = BasicUserSerializer(read_only=True)
    accept = serializers.SerializerMethodField()
    decline = serializers.SerializerMethodField()

    def get_delivery(self, obj):
        return DeliverySerializer(obj.delivery, context=self.context).data

    def get_accept(self, obj):
        request = self.context.get('request')
        if request:
            uri = request.build_absolute_uri(
                f'/api/{obj._meta.app_label}/{camel_to_snake(obj._meta.model.__name__)}/{obj.id}/accept'
            )
            return uri
        return None

    def get_decline(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(
                f'/api/{obj._meta.app_label}/{camel_to_snake(obj._meta.model.__name__)}/{obj.id}/decline'
            )
        return None

    class Meta:
        model = DeliveryRequest
        fields = "__all__"
        read_only_fields = (
            'id',
            'expired_at',
            'responded_at',
        )