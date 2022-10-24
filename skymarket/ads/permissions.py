from rest_framework.permissions import BasePermission
from users.models import UserRoles


class AdAdmin(BasePermission):
    message = 'Not permitted current user'

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRoles.ADMIN


class AdOwner(BasePermission):
    message = 'Not permitted current user'

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user and request.user and obj.author == request.user
