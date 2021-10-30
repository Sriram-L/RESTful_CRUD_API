from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from customers.models import Customers
from customers.serializers import CustomersSerializer


# Create your views here.

class customerApi(APIView):

    def get_customer(self, id):
        return get_object_or_404(Customers, customerId=id)

    def get(self, request, id):
        customerDetails = self.get_customer(id)
        customer_serializer = CustomersSerializer(customerDetails)
        return Response(customer_serializer.data)

    def put(self, request, id):
        customerDetails = self.get_customer(id)
        customer_serializer = CustomersSerializer(
            customerDetails, data=request.data)
        if (customer_serializer.is_valid()):
            customer_serializer.save()
            return Response(customer_serializer.data)
        return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        customerDetails = self.get_customer(id)
        customerDetails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class customerAddApi(APIView):
    def get(self, request):
        customerTable = Customers.objects.all()
        customer_serializer = CustomersSerializer(customerTable, many=True)
        return Response(customer_serializer.data)

    def post(self, request):
        customer_serializer = CustomersSerializer(
            data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response(customer_serializer.data, status=status.HTTP_201_CREATED)
        return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
