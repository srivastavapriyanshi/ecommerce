from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterView, MyObtainTokenPairView, CustomerListView, CustomerDetailView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('customer/register/', RegisterView.as_view(), name='customer-register'),
    path('admin/users/', CustomerListView.as_view(), name='admin-user-list'),
    path('admin/users/<int:pk>/', CustomerDetailView.as_view(), name='admin-user-detail'),
]
