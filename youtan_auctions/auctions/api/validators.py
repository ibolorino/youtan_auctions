from datetime import datetime

from rest_framework.serializers import ValidationError

from youtan_auctions.auctions.models import Properties_Bids, Vehicles_Bids

models = {"property": Properties_Bids, "vehicle": Vehicles_Bids}


def validate_bid(data, auction_item):
    value = data["value"]
    auction_item_instance = data[auction_item]
    minimum_increment = auction_item_instance.minimum_increment
    filter = {auction_item: auction_item_instance}
    bids = models[auction_item].objects.filter(**filter).order_by("-date")
    current_bid = auction_item_instance.initial_bid
    if bids:
        current_bid = bids[0].value

    auction_open(auction_item_instance.auction)
    multiple_bid(current_bid, value, minimum_increment)

    return data


def auction_open(auction):
    auction_date = auction.date
    if datetime.now().date() > auction_date:
        raise ValidationError({"auction": "The auction is closed."})


def multiple_bid(current_bid, value, minimum_increment):
    if value <= current_bid or (value - current_bid) % minimum_increment != 0:
        raise ValidationError(
            {
                "value": f"The bid must be an increment multiple of R$ {minimum_increment}."
            }
        )
