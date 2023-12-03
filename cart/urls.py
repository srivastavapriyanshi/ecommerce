from django.urls import path
from .views import CartView, add_to_cart, update_cart, remove_from_cart

urlpatterns = [
    path('customer/cart/', CartView.as_view(), name='cart-view'),
    path('customer/cart/add/', add_to_cart, name='add-to-cart'),
    path('customer/cart/update/', update_cart, name='update-cart'),
    path('customer/cart/remove/', remove_from_cart, name='remove-from-cart'),
]
