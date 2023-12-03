from rest_framework import serializers
from  .models import Cart, CartItem
from products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    sub_total = serializers.SerializerMethodField( method_name="total")

    class Meta:
        model= CartItem
        fields = ["id", "cart", "product", "quantity", "sub_total"]
        
    def total(self, cartitem:CartItem):
        return cartitem.quantity * cartitem.product.price

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'cart_items']

class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

class UpdateCartSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

class RemoveFromCartSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()