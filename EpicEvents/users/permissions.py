from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.groups.filter(name=["MANAGEMENT"]).exists():
            return True
        if user.groups.filter(name__in=["SALES", "SUPPORT"]):
            return request.method in permissions.SAFE_METHODS
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.groups.filter(name="MANAGEMENT").exists():
            return True
        if user.groups.filter(name__in=["SUPPORT", "SALES"]).exists():
            return request.method in permissions.SAFE_METHODS
        else:
            return False
