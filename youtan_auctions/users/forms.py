from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class UserCreateForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=255, required=True)
    username = forms.CharField(label="Username", max_length=255)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Senha", max_length=255, widget=forms.PasswordInput(render_value = True))
    password2 = forms.CharField(label="Repita sua senha", max_length=255, widget=forms.PasswordInput(render_value = True))
    is_superuser = forms.BooleanField(label="Super usuário")
    is_staff = forms.BooleanField(label="Membro da Equipe")
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({"placeholder": field.label})


class UserUpdateForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=255, required=True)
    username = forms.CharField(label="Username", max_length=255)
    email = forms.EmailField(label="Email")
    is_superuser = forms.BooleanField(label="Super usuário")
    is_staff = forms.BooleanField(label="Membro da Equipe")
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({"placeholder": field.label})


class UserChangePasswordForm(forms.Form):
    old_password = forms.CharField(label="Senha antiga", max_length=255, widget=forms.PasswordInput())
    password = forms.CharField(label="Nova senha", max_length=255, widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repita a nova senha", max_length=255, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs.update({"placeholder": field.label})