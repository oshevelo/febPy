from rest_framework import permissions

class IsSuperUserOrGetOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method=='GET' and obj.user==request.user:
            return True
        return False