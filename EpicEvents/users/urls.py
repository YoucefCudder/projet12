from rest_framework_simplejwt.views import TokenRefreshView

from .views import MyObtainTokenPairView, RegisterView
from django.urls import path


urlpatterns = [
    path("signup/", RegisterView.as_view(), name="auth_register"),
    path("login/", MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
