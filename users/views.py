
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics, permissions
from .serializers import RegisterSerializer, CustomerSerializer
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from permissions import IsAdmin

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.filter(role=User.CUSTOMER)
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CustomerListView(generics.ListCreateAPIView):
    queryset = User.objects.filter(role=User.CUSTOMER)
    serializer_class = CustomerSerializer
    permission_classes = [IsAdmin]

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role=User.CUSTOMER)
    serializer_class = CustomerSerializer
    permission_classes = [IsAdmin]

   