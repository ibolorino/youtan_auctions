from rest_framework.decorators import action
from rest_framework.response import Response


class BidActions:
    def create(self, request):
        message = {"detail": 'Method "POST" not allowed.'}
        return Response(message, status=405)

    def bid(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    @action(detail=False, methods=["post"])
    def property(self, request):
        return self.bid(request)

    @action(detail=False, methods=["post"])
    def vehicle(self, request):
        return self.bid(request)
