from django.db import models

from tax_api.constants import TAX_CODES

class TaxObject(models.Model):
    name = models.CharField(max_length=256)
    tax_code = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    def get_price(self):
        return float(self.price)

    def get_tax_type(self):
        return TAX_CODES[self.tax_code - 1]["type"]

    def get_refundable(self):
        return TAX_CODES[self.tax_code - 1]["refundable"]

    def get_tax_value(self):
        obj_price = self.get_price()
        return TAX_CODES[self.tax_code - 1]["value"](obj_price)

    def get_amount(self):
        return self.get_price() + self.get_tax_value()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tax Object"
        verbose_name_plural = "Tax Objects"