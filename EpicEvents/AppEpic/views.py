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

    def get_queryset(self, *args, **kwargs):
        if self.request.user.groups.filter(name="SALES").exists():
            return Client.objects.filter(sales_contact=self.request.user)

        if self.request.user.groups.filter(name="SUPPORT").exists():
            client_id = [
                event.client.id
                for event in Event.objects.filter(support_contact=self.request.user)
            ]
            return Client.objects.filter(event__in=client_id)


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [
        IsAuthenticated,
        ContractPermission,
    ]
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ["sales_contact", "amount", "client__email", "client__lastname", "created_at"]


    def get_queryset(self, *args, **kwargs):
        if self.request.user.groups.filter(name="SALES").exists():
            return Contract.objects.filter(sales_contact=self.request.user)

    def perform_create(self, serializer):
        if self.request.user.groups.filter(name="SALES").exists():
            return serializer.save(sales_contact=self.request.user)


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [
        IsAuthenticated,
        EventPermission,
    ]

    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ["event_date", "client__email", "client__lastname"]



    def get_queryset(self, *args, **kwargs):
        if self.request.user.groups.filter(name="SALES").exists():
            return Event.objects.filter(
                client__sales_contact=self.request.user
            )  # contract__sales_contact ?
        if self.request.user.groups.filter(name="SUPPORT").exists():
            event_id = [
                event.client.id
                for event in Event.objects.filter(support_contact=self.request.user)
            ]
            return Event.objects.filter(client__in=event_id)

    def perform_create(self, serializer):
        if self.request.user.groups.filter(name="SUPPORT").exists():
            return serializer.save(support_contact=self.request.user)

    def perform_update(self, serializer):
        if self.request.user.groups.filter(name="SUPPORT").exists():
            return serializer.save(support_contact=self.request.user)
