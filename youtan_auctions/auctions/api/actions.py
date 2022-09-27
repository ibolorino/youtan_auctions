from rest_framework.decorators import action
from rest_framework.response import Response

from youtan_auctions.auctions.models import Properties_Bids


class PropertyActions:
    """Custom actions for Property"""

    @action(detail=True, methods=["post"])
    def bid(self, request, pk):
        instance = self.get_object()
        new_bid = Properties_Bids(
            user=request.user, value=self.request.data.get("value"), property=instance
        )
        new_bid.save()

        return Response("ok", status=200)
