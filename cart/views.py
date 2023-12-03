from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from products.models import Product
from permissions import IsCustomer
from .serializers import CartSerializer, AddToCartSerializer, UpdateCartSerializer, RemoveFromCartSerializer

class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def get_object(self):
        # Retrieve the user's cart
        user_cart, created = Cart.objects.get_or_create(user=self.request.user)
        return user_cart

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsCustomer])
def add_to_cart(request):
    serializer = AddToCartSerializer(data=request.data)
    if serializer.is_valid():
        product_id = serializer.validated_data['product_id']
        quantity = serializer.validated_data['quantity']

        product = Product.objects.get(pk=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        cart_item.quantity += quantity
        cart_item.save()

        return Response({"message": "Item added to the cart successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsCustomer])
def update_cart(request):
    serializer = UpdateCartSerializer(data=request.data)
    if serializer.is_valid():
        item_id = serializer.validated_data['item_id']
        quantity = serializer.validated_data['quantity']
        cart_item = CartItem.objects.get(pk=item_id)
        cart_item.quantity = quantity
        cart_item.save()
        return Response({"message": "Cart updated successfully"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsCustomer])
def remove_from_cart(request):
    serializer = RemoveFromCartSerializer(data=request.data)
    if serializer.is_valid():
        item_id = serializer.validated_data['item_id']
        cart_item = CartItem.objects.get(pk=item_id)
        cart_item.delete()
        return Response({"message": "Item removed from the cart successfully"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
