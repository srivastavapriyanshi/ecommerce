from rest_framework import permissions
from users.models import User
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == User.ADMIN:
            return True
        return request.method in permissions.SAFE_METHODS


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.CUSTOMER


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.ADMIN