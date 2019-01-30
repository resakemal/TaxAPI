from rest_framework import serializers
from tax_api.models import TaxObject


class TaxObjectSerializer(serializers.ModelSerializer):
    tax_type = serializers.SerializerMethodField()
    refundable = serializers.SerializerMethodField()
    tax_value = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()

    def get_tax_type(self, obj):
        return obj.get_tax_type()

    def get_refundable(self, obj):
        return obj.get_refundable()

    def get_tax_value(self, obj):
        return obj.get_tax_value()

    def get_amount(self, obj):
        return obj.get_amount()

    class Meta:
        model = TaxObject
        fields = ('name', 'tax_code', 'price', 'tax_type', 'refundable', 'tax_value', 'amount')