from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ProductDetailView, ProductListView, CustomerProductDetailView, CustomerProductListView

urlpatterns = [

    path('admin/products/', ProductListView.as_view(), name='admin-product-list'),
    path('admin/products/<int:pk>/', ProductDetailView.as_view(), name='admin-product-detail'),
    path('customer/products/', CustomerProductListView.as_view(), name='customer-product-list'),
    path('customer/products/<int:pk>/', CustomerProductDetailView.as_view(), name='customer-product-detail'),
]
