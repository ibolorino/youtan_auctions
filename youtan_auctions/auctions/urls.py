from django.urls import path

from .views import (
    home_page,
    auctions_list_view,
    auctions_create_view,
    auctions_update_view,
    auctions_items_list_view,
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
]
