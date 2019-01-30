import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from tax_api.models import TaxObject


class TaxObjectViewTest(TestCase):
    def test_post_view(self):
        data = {
            "name": "Pizza",
            "tax_code": 1,
            "price": 100
        }
        url = reverse("tax-object")
        result = self.client.post(url, json.dumps(
            data), content_type="application/json")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        tax_obj = TaxObject.objects.get(name="Pizza")
        self.assertEqual(tax_obj.name, "Pizza")
        self.assertEqual(tax_obj.tax_code, 1)
        self.assertEqual(tax_obj.price, 100)

    def test_invalid_tax_code(self):
        data = {
            "name": "Apartment",
            "tax_code": 4,
            "price": 10000
        }
        url = reverse("tax-object")
        result = self.client.post(url, json.dumps(
            data), content_type="application/json")
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_view(self):
        self.tax_obj = TaxObject.objects.create(
            name="Pizza", tax_code=1, price=100
        )
        self.tax_obj = TaxObject.objects.create(
            name="Cigarettes", tax_code=2, price=50
        )
        self.tax_obj = TaxObject.objects.create(
            name="Balloons", tax_code=3, price=300
        )
        url = reverse("tax-object")
        result = self.client.get(url)
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        tax_obj = TaxObject.objects.get(name="Pizza")
        self.assertEqual(tax_obj.name, "Pizza")
        self.assertEqual(tax_obj.tax_code, 1)
        self.assertEqual(tax_obj.price, 100)