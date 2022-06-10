from rest_framework import permissions


class IsOwnerOrPutOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT':
            True
        return obj.owner == request.user

