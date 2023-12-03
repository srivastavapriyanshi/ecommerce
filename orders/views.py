from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Order, OrderItem
from users.models import User
from users.serializers import CustomerSerializer
from products.models import Product
from products.serializers import ProductSerializer
from permissions import IsAdmin, IsCustomer
from .serializers import  OrderSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from cart.models import Cart
from .serializers import OrderSerializer, CreateOrderSerializer, UpdateOrderSerializer

class OrderCustomerListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsCustomer]


    def get_queryset(self):
        # Retrieve the orders for the authenticated user
        return Order.objects.filter(user=self.request.user)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsCustomer])
def create_order(request):
    serializer = CreateOrderSerializer(data=request.data, context={'request': request})
    
    if serializer.is_valid():
        order = serializer.save()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderAdminListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


    def get_queryset(self):
        return Order.objects.all()

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdmin])
def update_order(request):
    serializer = UpdateOrderSerializer(data=request.data)
    if serializer.is_valid():
        order_id = serializer.validated_data['order_id']
        order = Order.objects.get(pk=order_id)
        print(serializer.validated_data)
        order.status = serializer.validated_data['status']
        order.save()
        return Response({"message": "Cart updated successfully"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

