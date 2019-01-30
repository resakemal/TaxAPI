from django.test import TestCase

from tax_api.models import TaxObject


class TaxObjectModelTest(TestCase):
    def test_create_tax_object(self):
        TaxObject.objects.create(
            name="Pizza", tax_code=1, price=100
        )

        tax_obj = TaxObject.objects.get(name="Pizza")
        self.assertEqual(tax_obj.name, "Pizza")
        self.assertEqual(tax_obj.tax_code, 1)
        self.assertEqual(tax_obj.price, 100)

    def test_duplicate_tax_object(self):
        TaxObject.objects.create(
            name="Pizza", tax_code=1, price=100
        )
        TaxObject.objects.create(
            name="Pizza", tax_code=1, price=100
        )

        tax_objects = TaxObject.objects.filter(name="Pizza")
        self.assertEqual(len(tax_objects), 2)

    def test_tax_object_attributes(self):
        tax_obj_1 = TaxObject.objects.create(
            name="Pizza", tax_code=1, price=100
        )
        self.assertEqual(tax_obj_1.get_tax_type(), "Food")
        self.assertTrue(tax_obj_1.get_refundable())
        self.assertEqual(tax_obj_1.get_tax_value(), 10)
        self.assertEqual(tax_obj_1.get_amount(), 110)

        tax_obj_2 = TaxObject.objects.create(
            name="Cigarettes", tax_code=2, price=50
        )
        self.assertEqual(tax_obj_2.get_tax_type(), "Tobacco")
        self.assertFalse(tax_obj_2.get_refundable())
        self.assertEqual(tax_obj_2.get_tax_value(), 11)
        self.assertEqual(tax_obj_2.get_amount(), 61)

        tax_obj_3 = TaxObject.objects.create(
            name="Balloons", tax_code=3, price=300
        )
        self.assertEqual(tax_obj_3.get_tax_type(), "Entertainment")
        self.assertFalse(tax_obj_3.get_refundable())
        self.assertEqual(tax_obj_3.get_tax_value(), 2)
        self.assertEqual(tax_obj_3.get_amount(), 302)