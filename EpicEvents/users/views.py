from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializer
from django.contrib.auth.models import Group
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
        serializer.save(
            username=self.request.data.get('username'),
            email=self.request.data.get('email'),
            password=make_password(self.request.data.get('password')),
            groups=self.request.data.get('groups'),
        )
        if User.groups == 'MANAGEMENT':
            group = Group.objects.get(name='MANAGEMENT')
            group.user_set.add(serializer.instance)
        elif User.groups == 'SALES':
            group = Group.objects.get(name='SALES')
            group.user_set.add(serializer.instance)
        elif User.groups == 'SUPPORT':
            group = Group.objects.get(name='SUPPORT')
            group.user_set.add(serializer.instance)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated, UserPermission]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, UserPermission]
