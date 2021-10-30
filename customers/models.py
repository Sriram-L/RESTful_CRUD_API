from django.db import models

# Create your models here.


class Customers(models.Model):
    customerId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=500)
    lastName = models.CharField(max_length=500)
    emailId = models.EmailField()
    mobileNo = models.CharField(max_length=20)
    city = models.CharField(max_length=500)
    address = models.TextField()
