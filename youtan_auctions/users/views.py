from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, TemplateView
from youtan_auctions.auctions.mixins import AdminMixin
from .forms import UserCreateForm, UserUpdateForm, UserChangePasswordForm

User = get_user_model()


class UserListView(AdminMixin, TemplateView):
    template_name = "users/list_users.html"


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


class UserCreateView(AdminMixin, TemplateView):
    template_name = "users/create_user.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserCreateForm()
        return context


class UserUpdateView(AdminMixin, DetailView):
    template_name = "users/update_user.html"
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['form'] = UserUpdateForm(instance.__dict__)
        context['object_id'] = instance.id
        return context


class UserChangePasswordView(LoginRequiredMixin, TemplateView):
    template_name = "users/change_password.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserChangePasswordForm()
        return context


user_list_view = UserListView.as_view()
user_detail_view = UserDetailView.as_view()
user_update_view = UserUpdateView.as_view()
user_create_view = UserCreateView.as_view()
user_update_view = UserUpdateView.as_view()
user_change_password_view = UserChangePasswordView.as_view()
