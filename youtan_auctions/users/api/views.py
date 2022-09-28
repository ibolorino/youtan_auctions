from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from youtan_auctions.auctions.permissions import UserViewSetPermission

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [UserViewSetPermission]

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        queryset = User.objects.all()
        if not self.request.user.is_staff:
            queryset = queryset.filter(id=self.request.user.id)
        print(queryset)
        return queryset
