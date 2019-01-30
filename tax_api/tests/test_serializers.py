from django.test import TestCase

from tax_api.models import TaxObject
from tax_api.serializers import TaxObjectSerializer


class TaxObjectSerializerTest(TestCase):
    def test_serializer(self):
        tax_data = dict(name="Pizza", tax_code=1, price=100)
        ser = TaxObjectSerializer(data=tax_data)
        self.assertTrue(ser.is_valid())
