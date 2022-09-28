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
            "is_staff",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_staff": {"read_only": True},
        }

    def validate(self, data):
        if data.get("password") != data.get("password2"):
            raise serializers.ValidationError(
                {"password": ["The passwords must be the same."]}
            )
        data.pop("password2", None)
        return data

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_email(self, value):
        is_valid_email(value)
        return value

    def validate_password(self, value):
        is_valid_password(value)
        return value
