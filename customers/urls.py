from django.urls import path
from .views import customerAddApi, customerApi

"""Contains the url patterns used to route each method"""

urlpatterns = [
    path('customers/', customerAddApi.as_view(), name='add_customer'),
    path('customers/<int:id>/', customerApi.as_view(),
         name='get_put_delete_customer')
]
