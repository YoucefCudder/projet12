from rest_framework.viewsets import ModelViewSet

from AppEpic.models import Client, Contract, Event
from AppEpic.serializer import ContractSerializer, EventSerializer, ClientSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes =


class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    # permission_classes =
    # filterset_fields = ['sales_contact']


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = []
