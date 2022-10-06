from django.urls import path

from youtan_auctions.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    user_list_view,
    user_create_view,
)

app_name = "users"
urlpatterns = [
    path("", user_list_view, name="list-users"),
    path("create/", user_create_view, name="create-user"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
