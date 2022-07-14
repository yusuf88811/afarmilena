from rest_framework import serializers

from service.models.order import Order


class OrderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["total_price", "people_count", "menu", "user", "wedding_hall", "service", "menu_price", "service_price", "status"]


class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["total_price", "people_count", "menu", "wedding_hall", "service"]
