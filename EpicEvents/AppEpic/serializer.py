from rest_framework import serializers

from AppEpic.models import Client, Contract, Event


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'firstname', 'lastname', 'email', 'phone', 'mobile', 'company_name',
                  "sales_contact"]  # 'sales_contact'

    extra_kwargs = {
        "date_created": {"required": True},
        "date_updated": {"required": True},
    }

    # def validate_sales_contact(self, sales_contact):
    #     if not sales_contact.groups.filter(name="sales").exists():
    #         raise serializers.ValidationError("Sales_contact must be in group sales!")
    #     else:
    #         return sales_contact

    def create(self, validated_data):
        client = Client.objects.create(**validated_data)
        return client


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'sales_contact', 'client', 'status', 'amount', 'payment', 'created_at',
                  'updated_at']

    def create(self, validated_data):
        contract = Contract.objects.create(**validated_data)
        event = Event.objects.create(contract=contract,
                                     client=contract.client)  # event directement créé, contrat = 1 event au min
        #
        contract.save()
        #
        event.save()
        return contract


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['client', 'created_at', 'updated_at', 'support_contact', 'event_status', 'attendees',
                  'event_date', 'notes']
        read_only_fields = ['client']
