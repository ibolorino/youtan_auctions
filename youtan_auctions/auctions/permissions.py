from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    """
    Custom permission to views.
    Allow authenticated users on safe methods;
    Allow authenticated users on allowed_actions;
    Allow admin users on all methods
    """

    def has_permission(self, request, view):
        return bool(
            (
                request.user
                and request.user.is_authenticated
                and request.method in permissions.SAFE_METHODS
            )  # user is authenticated and method is safe
            or (request.user and request.user.is_staff)  # user is admin
            or (
                request.user
                and request.user.is_authenticated
                and view.allowed_actions
                and view.action in view.allowed_actions
            )  # user is authenticated and actions is allowed
        )
