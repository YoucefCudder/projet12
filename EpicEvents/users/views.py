from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializer
from django.contrib.auth.models import Group

from .models import WorkingTeam
from .permissions import UserPermission
from .serializer import RegisterSerializer, GroupSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = serializer.MyTokenObtainPairSerializer


class RegisterView(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializer.RegisterSerializer

    def perform_create(self, serializer):
        # user = User.objects.create(serializer)
        # user.groups.set()
        # user.set_password(["password"])
        user = User.objects.all()
        print(user)
        print(serializer)
        # if serializer == "MANAGEMENT":
        #     user.is_staff = True
        serializer.save()

        return user


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated, UserPermission]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, UserPermission]

    def is_staff(self):
        # return [user.is_staff is True in User.groups.name for user in User.groups.filter(name="MANAGEMENT")]1er essai
        # for user in Group.objects.filter(name="MANAGEMENT"): 2eme essai
        #     user.is_staff = True
        # user = User.objects.all()
        # for _ in user.groups.name == "MANAGEMENT": 3e essai
        #     user.is_staff = True
        pass
