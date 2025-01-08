from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class CheckDoctorTrue(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'doctor':
            return True
        return False


class CheckDoctorTrue(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'doctor':
            return True
        return False



class CheckDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'doctor':
            return False
        return True

