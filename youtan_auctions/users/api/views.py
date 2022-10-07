from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from youtan_auctions.auctions.permissions import UserViewSetPermission
from youtan_auctions.auctions.models import Properties_Bids, Vehicles_Bids

from .serializers import UserSerializer, UserChangePasswordSerializer
from .actions import UserActions

User = get_user_model()


class UserViewSet(UserActions, ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [UserViewSetPermission]

    def get_serializer_class(self):
        if self.action == "change_password":
            return UserChangePasswordSerializer
        return UserSerializer

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        queryset = User.objects.all()
        if not self.request.user.is_staff:
            queryset = queryset.filter(id=self.request.user.id)
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance == request.user:
            return Response("Não é possível excluir o usuário logado.", status=400)
        self.perform_destroy(instance)
        return Response(status=204)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)