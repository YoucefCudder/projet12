from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.fields import BooleanField
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import WorkingTeam


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token["username"] = user.username
        return token


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingTeam
        fields = ["id", "name"]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    is_active = serializers.BooleanField(default=True)
    groups = serializers.CharField(required=True)
    is_staff = BooleanField(label="Staff status", required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "is_active",
            "is_staff",
            "groups",
        ]
        extra_kwargs = {
            "date_created": {"required": True},
            "date_updated": {"required": True},
        }

    #
    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username=validated_data["username"],
    #         email=validated_data["email"],
    #         first_name=validated_data["first_name"],
    #         last_name=validated_data["last_name"],
    #     )
    #     user.groups.set(validated_data["groups"])
    #     user.set_password(validated_data["password"])
    #
    #     user.save()
    #
    #     return user
