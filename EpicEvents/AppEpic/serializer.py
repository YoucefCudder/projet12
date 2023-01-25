from rest_framework import serializers

from AppEpic.models import Client, Contract, Event


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "firstname",
            "lastname",
            "email",
            "phone",
            "mobile",
            "company_name",
            "sales_contact",
        ]

    extra_kwargs = {
        "date_created": {"required": True},
        "date_updated": {"required": True},
    }


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
