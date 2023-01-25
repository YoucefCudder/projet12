from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from AppEpic.models import Client, Event, Contract
from AppEpic.permissions import ClientPermission, ContractPermission, EventPermission
from AppEpic.serializer import ContractSerializer, EventSerializer, ClientSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, ClientPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["firstname", "lastname", "email"]

    def perform_create(self, serializer):
        return serializer.save(sales_contact=self.request.user)

    def get_queryset(self):
        return Client.objects.all()


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [
        IsAuthenticated,
        EventPermission,
    ]

    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ["event_date", "client__email", "client__lastname"]

    def get_queryset(self):
        return Event.objects.all()

    def perform_create(self, serializer):

        if self.request.user.groups.filter(name="SUPPORT").exists():
            return serializer.save(support_contact=self.request.user)


    def perform_update(self, serializer):
        if self.request.user.groups.filter(name="SUPPORT").exists():
            return serializer.save(support_contact=self.request.user)


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [
        IsAuthenticated,
        ContractPermission,
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["sales_contact", "amount", "client__email", "client__lastname", "created_at"]

    def get_queryset(self):
        return Contract.objects.all()

    def perform_create(self, serializer):
        if self.request.user.groups.filter(name="SALES").exists():
            return serializer.save(sales_contact=self.request.user)
 
