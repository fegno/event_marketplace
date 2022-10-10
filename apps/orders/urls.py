from django.urls import path, include

from apps.orders.views import order_payment, callback, pay
from apps.user.views import *

urlpatterns = [
    path("", pay, name="pay"),
    path("payment/", order_payment, name="payment"),
    path("callback/", callback, name="callback"),
]