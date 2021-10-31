import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Customers
from ..serializers import CustomersSerializer

# initializing the client app for testing

client = Client()


class getCustomer(TestCase):
    """GET request for retriving single customer"""

    def setUp(self):
        self.bot1 = Customers.objects.create(
            firstName='bot1', lastName='test', emailId='bot@botmail.com', mobileNo='200', city='botcity', address='botland')
        self.bot2 = Customers.objects.create(
            firstName='bot2', lastName='test', emailId='bot@botmail.com', mobileNo='200', city='botcity', address='botland')
        self.bot3 = Customers.objects.create(
            firstName='bot3', lastName='test', emailId='bot@botmail.com', mobileNo='200', city='botcity', address='botland')
        self.bot4 = Customers.objects.create(
            firstName='bot4', lastName='test', emailId='bot@botmail.com', mobileNo='200', city='botcity', address='botland')

    def test_valid_get_customer(self):
        apiResponse = client.get(
            reverse('get_put_delete_customer', kwargs={'id': self.bot1.customerId}))
        customerDetails = Customers.objects.get(
            customerId=self.bot1.customerId)
        customerSerializer = CustomersSerializer(customerDetails)
        self.assertEqual(apiResponse.data, customerSerializer.data)
        self.assertEqual(apiResponse.status_code, status.HTTP_200_OK)

    def test_invalid_get_customer(self):
        apiResponse = client.get(
            reverse('get_put_delete_customer', kwargs={'id': 10}))
        self.assertEqual(apiResponse.status_code, status.HTTP_404_NOT_FOUND)


class putCustomer(TestCase):
    """PUT request to update existing customer"""

    def setUp(self):
        self.bot5 = Customers.objects.create(
            firstName='bot5', lastName='test', emailId='bot@botmail.com', mobileNo='200', city='botcity', address='botland')
        self.bot6 = Customers.objects.create(
            firstName='bot6', lastName='test', emailId='bot@botmail.com', mobileNo='200', city='botcity', address='botland')
        self.valid_json = {
            'customerId': 5,
            'firstName': 'bot5',
            'lastName': 'noTest',
            'emailId': 'bot@botmail.com',
            'mobileNo': '200',
            'city': 'botcity',
            'address': 'botland'
        }
        self.invalid_json = {
            'customerId': 5,
            'firstName': '',
            'lastName': 'noTest',
            'emailId': 'bot@botmail.com',
            'mobileNo': '200',
            'city': 'botcity',
            'address': 'botland'
        }

    def test_valid_put_customer(self):
        apiResponse = client.put(reverse('get_put_delete_customer', kwargs={'id': self.bot5.customerId}),
                                 data=json.dumps(self.valid_json),
                                 content_type='application/json'
                                 )
        self.assertEqual(apiResponse.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_put_customer(self):
        apiResponse = client.put(reverse('get_put_delete_customer', kwargs={'id': self.bot5.customerId}),
                                 data=json.dumps(self.invalid_json),
                                 content_type='application/json'
                                 )
        self.assertEqual(apiResponse.status_code, status.HTTP_400_BAD_REQUEST)


class deleteCustomer(TestCase):
    """DELETE request to delete existing customer"""

    def setUp(self):
        self.bot7 = Customers.objects.create(
            firstName='bot5', lastName='test', emailId='bot@botmail.com', mobileNo='200', city='botcity', address='botland')

    def test_valid_delete_customer(self):
        apiResponse = client.delete(
            reverse('get_put_delete_customer', kwargs={'id': self.bot7.customerId}))
        self.assertEqual(apiResponse.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_customer(self):
        apiResponse = client.delete(
            reverse('get_put_delete_customer', kwargs={'id': 10}))
        self.assertEqual(apiResponse.status_code, status.HTTP_404_NOT_FOUND)


class postCustomer(TestCase):
    """POST request to create a new customer in database"""

    def setUp(self):
        self.valid_json = {
            'firstName': 'bot8',
            'lastName': 'noTest',
            'emailId': 'bot@botmail.com',
            'mobileNo': '200',
            'city': 'botcity',
            'address': 'botland'
        }
        self.invalid_json = {
            'firstName': '',
            'lastName': 'noTest',
            'emailId': 'bot@botmail.com',
            'mobileNo': '200',
            'city': 'botcity',
            'address': 'botland'
        }

    def test_valid_post_customer(self):
        apiResponse = client.post(reverse('add_customer'),
                                  data=json.dumps(self.valid_json),
                                  content_type='application/json'
                                  )
        self.assertEqual(apiResponse.status_code, status.HTTP_201_CREATED)

    def test_invalid_post_customer(self):
        apiResponse = client.post(reverse('add_customer'),
                                  data=json.dumps(self.invalid_json),
                                  content_type='application/json'
                                  )
