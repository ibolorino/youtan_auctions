from django.urls import path

from .views import (
    home_page,
    auctions_list_view,
    auctions_create_view,
    auctions_update_view,
    auctions_items_list_view,
    property_create_view,
    all_items_list_view,
    property_update_view,
    vehicle_create_view,
    vehicle_update_view,
    property_detail_view,
    vehicle_detail_view,
    bank_create_view,
    bank_list_view,
)

app_name = "auctions"

urlpatterns = [
    path(
        "",
        home_page,
        name="home-page",
    ),
    path("auctions/", auctions_list_view, name="list-auctions"),
    path("auctions/create/", auctions_create_view, name="create-auction"),
    path("auctions/<int:pk>/update/", auctions_update_view, name="update-auction"),
    path("auctions/<int:pk>/items/", auctions_items_list_view, name="update-auction"),
    path("items/", all_items_list_view, name="list-items"),
    path("properties/<int:pk>/", property_detail_view, name="detail-property"),
    path("properties/create/", property_create_view, name="create-property"),
    path("properties/<int:pk>/update/", property_update_view, name="update-property"),
    path("vehicles/<int:pk>/", vehicle_detail_view, name="detail-vehicle"),
    path("vehicles/create/", vehicle_create_view, name="create-vehicle"),
    path("vehicles/<int:pk>/update/", vehicle_update_view, name="update-vehicle"),
    path("banks/", bank_list_view, name="list-banks"),
    path("banks/create/", bank_create_view, name="create-bank"),
]
