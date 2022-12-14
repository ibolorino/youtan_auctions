from rest_framework import permissions
from youtan_auctions.users.models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to views.
    Allow authenticated users on safe methods;
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
        )


class UserViewSetPermission(permissions.BasePermission):
    """
    Pemrission class for UserViewSet
    Allow only unauthenticated users to Create method
    Allow only authenticated users on all other methods
    """

    def has_permission(self, request, view):
        if view.action in ("update", "partial_update", "destroy"):
            return request.user and request.user.is_staff
        if view.action == "change_password":
            pk = view.kwargs.get("pk")
            return request.user.is_authenticated and request.user in User.objects.filter(pk=pk)
        return request.user and request.user.is_authenticated
