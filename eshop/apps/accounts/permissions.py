from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated


class IsSuperUserOrSafeOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in SAFE_METHODS and obj.user==request.user:
            return True
        return False