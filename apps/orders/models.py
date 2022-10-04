from django.conf import settings
from django.db import models


class ModeOfPayment(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)


class Currency(models.Model):
    pre_text = models.CharField(max_length=6)
    post_text = models.CharField(max_length=6)
    symbol = models.CharField(max_length=6)
    country = models.CharField(max_length=60)


# Create your models here.
class Inquiry(models.Model):
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Order(models.Model):
    PLACED = "Placed"
    CANCELLED = "Cancelled"
    PARTIAL_RETURN = "Returned Partially"

    status = models.CharField(max_length=22, choices=[
        (PLACED, PLACED),
        (CANCELLED, CANCELLED),
        (PARTIAL_RETURN, PARTIAL_RETURN),
    ])

    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    mode_of_payment = models.ForeignKey(ModeOfPayment, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField(default=0)
    amount_discount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    net_amount = models.FloatField(default=0)

    transaction_id = models.CharField(max_length=100)
    payment_gateway_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Ticket(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets')
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name='tickets')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
