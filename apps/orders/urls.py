from django.urls import path, include

from apps.orders.views import order_payment, callback
from apps.user.views import *

urlpatterns = [
    path("payment/", order_payment, name="payment"),
    path("callback/", callback, name="callback"),
]