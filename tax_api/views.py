from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tax_api.models import TaxObject
from tax_api.serializers import TaxObjectSerializer
from tax_api.constants import TAX_CODES


class TaxObjectView(APIView):
    serializer_class = TaxObjectSerializer

    def get(self, request, format=None):
        tax_objects = TaxObject.objects.all()
        ser = TaxObjectSerializer(tax_objects, many=True)
        data = ser.data

        price_total = tax_total = 0.0
        for obj in data:
            price_total += float(obj["price"])
            tax_total += float(obj["tax_value"])
        grand_total = price_total + tax_total
        data.append(
            {
                "total": {
                    "price_total": price_total,
                    "tax_total": tax_total,
                    "grand_total": grand_total
                }
            }
        )

        return Response(data)

    def post(self, request, format=None):
        try:
            # Check if tax_code is in range of available tax codes
            tax_code = request.data["tax_code"]
            if (1 <= int(tax_code) <= len(TAX_CODES)):
                ser = TaxObjectSerializer(data=request.data)
                if ser.is_valid():
                    ser.save()
                    return Response(ser.data, status=status.HTTP_201_CREATED)
            raise Exception("Unknown tax code")
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)