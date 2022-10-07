from django.contrib.auth.password_validation import (
    validate_password as is_valid_password,
)
from django.core.validators import validate_email as is_valid_email
from rest_framework import serializers

from youtan_auctions.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "username",
            "email",
            "password",
            "password2",
            "is_superuser",
            "is_staff",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, data):
        if data.get("password") != data.get("password2"):
            raise serializers.ValidationError(
                {"password": ["The passwords must be the same."]}
            )
        data.pop("password2", None)

        if "is_staff" not in data:
            data["is_staff"] = False
        if "is_superuser" not in data:
            data["is_superuser"] = False
        
        return data

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_email(self, value):
        is_valid_email(value)
        action = self.context["request"].parser_context["view"].action
        if User.objects.filter(email=value).exists() and action not in ("update", "partial_update"):
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_password(self, value):
        is_valid_password(value)
        return value


class UserChangePasswordSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    old_password = serializers.CharField(style={"input_type": "password"}, write_only=True, required=True)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "old_password",
            "password",
            "password2",
        ]

    def validate(self, data):
        if data.get("password") != data.get("password2"):
            raise serializers.ValidationError(
                {"password": ["The passwords must be the same."]}
            )
        data.pop("password2", None)

        return data

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("Incorrect password.")
        return value

    def validate_password(self, value):
        is_valid_password(value)
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance