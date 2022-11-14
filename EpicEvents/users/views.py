from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializer
from django.contrib.auth import get_user_model

from .serializer import RegisterSerializer, User


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = serializer.MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializer.RegisterSerializer





class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    # permission_classes =


