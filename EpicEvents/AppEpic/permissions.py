from rest_framework import permissions


class ClientPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method == "DELETE":
            return False
        user = request.user
        if user.groups.filter(name="SALES").exists():
            return True
        if user.groups.filter(name__in=["SUPPORT", "MANAGEMENT"]):
            return request.method in permissions.SAFE_METHODS
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.groups.filter(name="SALES").exists():
            return True
        if user.groups.filter(name__in=["SUPPORT", "MANAGEMENT"]):
            return request.method in permissions.SAFE_METHODS
        else:
            return False


class ContractPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE":
            return False
        user = request.user
        if user.groups.filter(name="SALES").exists():
            return True
        if user.groups.filter(name__in=["SUPPORT", "MANAGEMENT"]).exists():
            return request.method in permissions.SAFE_METHODS
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.groups.filter(name="SALES").exists():
            return request.method in ["POST", "GET", "PUT"]
        if user.groups.filter(name__in=["SUPPORT", "MANAGEMENT"]).exists():
            return request.method in permissions.SAFE_METHODS
        else:
            return False


class EventPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE":
            return False
        user = request.user
        if user.groups.filter(name="SALES").exists():
            return True
        if user.groups.filter(name="MANAGEMENT").exists():
            return request.method in permissions.SAFE_METHODS
        if user.groups.filter(name="SUPPORT").exists():
            return request.method in ["GET", "PUT"]
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.groups.filter(name="SALES").exists():
            return request.method in ["GET", "PUT"]
        if user.groups.filter(name="MANAGEMENT").exists():
            return request.method in permissions.SAFE_METHODS
        if user.groups.filter(name="SUPPORT").exists():
            if user == obj.support_contact and obj.event_status is True:
                return request.method in ["GET", "PUT"]
        else:
            return False
