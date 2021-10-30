from django.urls import path
from .views import customerAddApi, customerApi

urlpatterns = [
    path('customers/', customerAddApi.as_view()),
    path('customers/<int:id>/', customerApi.as_view())
]
