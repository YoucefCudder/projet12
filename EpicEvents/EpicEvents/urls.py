"""EpicEvents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

import users
from AppEpic.views import EventViewSet, ClientViewSet, ContractViewSet
from users.views import UserViewSet, GroupViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
#
router.register(r"clients", ClientViewSet, basename="Client")
router.register(r"contracts", ContractViewSet, basename="Contract")
router.register(r"events", EventViewSet, basename="Event")

router.register(r"groups", GroupViewSet)
def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path("admin/", admin.site.urls),
    path('debug/', trigger_error),
    path("api/", include(router.urls)),
    path("", include("users.urls")),
]
