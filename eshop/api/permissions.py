from rest_framework import permissions


class BaseNoObjectPermission(permissions.BasePermission):
    """ Base class for all permission classes, where permissions are determined
        by view kwargs (such as 'profile_id' etc.)
    """

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class RequestIsReadOnly(BaseNoObjectPermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class RequestIsCreate(BaseNoObjectPermission):

    def has_permission(self, request, view):
        return request.method == 'POST'


class RequestIsUpdate(BaseNoObjectPermission):

    def has_permission(self, request, view):
        return request.method in ['PUT', 'PATCH']


class RequestIsDelete(BaseNoObjectPermission):

    def has_permission(self, request, view):
        return request.method == 'DELETE'
