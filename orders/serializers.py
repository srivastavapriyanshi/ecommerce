from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.IntegerField()

    def create(self, validated_data):
        cart_id = validated_data['cart_id']
        user = self.context['request'].user
        cart = Cart.objects.get(id=cart_id, user=user)
        order = Order.objects.create(user=user, total_amount=0) 
        for cart_item in cart.cart_items.all():
            OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
        cart.cart_items.all().delete()
        return order

class UpdateOrderSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField()
    status = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ('order_id', 'status')