from rest_framework.permissions import BasePermission
from rest_framework import permissions

class CheckOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.role_user == 'ownerUser':
            return False
        return True


class CheckCrud(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role_user == 'ownerUser'