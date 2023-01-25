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

    def validate(self, attrs):
        if attrs['status'] is False:
            raise serializers.ValidationError("Client is required")
        return attrs


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['client', 'created_at', 'updated_at', 'support_contact', 'event_status', 'attendees',
                  'event_date', 'notes', 'contract']
        read_only_fields = ['client']

    def validate(self, attrs):
        if attrs['contract'] is None:
            raise serializers.ValidationError("Contract related is required")
        return attrs
