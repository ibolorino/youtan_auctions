from django.urls import path

from youtan_auctions.users.views import (
    user_update_view,
    user_list_view,
    user_create_view,
    user_change_password_view
)

app_name = "users"
urlpatterns = [
    path("", user_list_view, name="list-users"),
    path("create/", user_create_view, name="create-user"),
    path("<int:pk>/update/", user_update_view, name="update-user"),
    path("change_password/", user_change_password_view, name="change-password"),
]
