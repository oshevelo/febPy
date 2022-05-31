from rest_framework import permissions


class IsEditable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or obj.editor == request.user or request.user.is_superuser


class IsOwnedBy(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_superuser
