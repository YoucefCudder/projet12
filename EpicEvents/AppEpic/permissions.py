from rest_framework import permissions


class ClientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return False
        user = request.user
        print(user.team)
        if user.team.filter(name='SALES').exists():
            return True
        if user.team.filter(name__in=['SUPPORT', 'MANAGEMENT']):
            return request.method in permissions.SAFE_METHODS
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.team.filter(name="SALES").exists():
            return True
        if user.team.filter(name__in=['SUPPORT', 'MANAGEMENT']):
            return request.method in permissions.SAFE_METHODS
        else:
            return False