from rest_framework.decorators import action
from rest_framework.response import Response


class UserActions:
    
    @action(detail=True, methods=["PATCH"])
    def change_password(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=200, headers=headers)