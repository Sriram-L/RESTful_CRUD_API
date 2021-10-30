from rest_framework import serializers
from customers.models import Customers


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('customerId', 'firstName', 'lastName',
                  'emailId', 'mobileNo', 'city', 'address')
