from rest_framework import permissions

class IsSuperUserOrSafeOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in ('GET','HEAD', 'OPTIONS') and obj.user==request.user:
            return True
        return False