# urls.py
from django.urls import path
from .views import OrderCustomerListView, OrderAdminListView, create_order, update_order

urlpatterns = [
    path('customer/orders/', OrderCustomerListView.as_view(), name='customer-order-list'),
    path('admin/orders/', OrderAdminListView.as_view(), name='admin-order-list'),
    path('customer/orders/create/', create_order, name='create-order'),
    path('admin/orders/update/', update_order, name='update-order'),

]
