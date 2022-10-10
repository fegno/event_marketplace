from django.conf import settings
from django.db import models
from decimal import Decimal
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField


# Create your models here.


class PaymentStatus:
    SUCCESS = "Success"
    FAILURE = "Failure"
    PENDING = "Pending"



def get_default_currency():
    return settings.DEFAULT_CURRENCY


def currency(value, currency):
    if not currency:
        currency = settings.DEFAULT_CURRENCY
    return value


class Transaction(models.Model):
    """
    A transaction for a particular payment source.

    These are similar to the payment events within the order app but model a
    slightly different aspect of payment.  Crucially, payment sources and
    transactions have nothing to do with the lines of the order while payment
    events do.

    For example:
    * A ``pre-auth`` with a bankcard gateway
    * A ``settle`` with a credit provider (see :py:mod:`django-oscar-accounts`)
    """
    source = models.ForeignKey(
        'payment.Source',
        on_delete=models.CASCADE,
        related_name='transactions',
        verbose_name=_("Source"))

    # We define some sample types but don't constrain txn_type to be one of
    # these as there will be domain-specific ones that we can't anticipate
    # here.
    AUTHORISE, DEBIT, REFUND = 'Authorise', 'Debit', 'Refund'
    txn_type = models.CharField(_("Type"), max_length=128, blank=True)

    amount = models.DecimalField(_("Amount"), decimal_places=2, max_digits=12)
    reference = models.CharField(_("Reference"), max_length=128, blank=True)
    status = models.CharField(_("Status"), max_length=128, blank=True)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True, db_index=True)

    def __str__(self):
        return _("%(type)s of %(amount).2f") % {
            'type': self.txn_type,
            'amount': self.amount}

    class Meta:
        app_label = 'payment'
        ordering = ['-date_created']
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")


class SourceType(models.Model):
    """
    A type of payment source.

    This could be an external partner like PayPal or DataCash,
    or an internal source such as a managed account.
    """
    name = models.CharField(_("Name"), max_length=128, db_index=True)
    code = AutoSlugField(
        _("Code"), max_length=128, populate_from='name', unique=True,
        help_text=_("This is used within forms to identify this source type"))

    class Meta:
        app_label = 'payment'
        ordering = ['name']
        verbose_name = _("Source Type")
        verbose_name_plural = _("Source Types")

    def __str__(self):
        return self.name

class Source(models.Model):
    """
    A source of payment for an order.

    This is normally a credit card which has been pre-authorised for the order
    amount, but some applications will allow orders to be paid for using
    multiple sources such as cheque, credit accounts, gift cards. Each payment
    source will have its own entry.

    This source object tracks how much money has been authorised, debited and
    refunded, which is useful when payment takes place in multiple stages.
    """
    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
        related_name='sources',
        verbose_name=_("Order"))
    source_type = models.ForeignKey(
        'payment.SourceType',
        on_delete=models.CASCADE,
        related_name="sources",
        verbose_name=_("Source Type"))
    currency = models.CharField(
        _("Currency"), max_length=12, default=get_default_currency)

    # Track the various amounts associated with this source
    amount_allocated = models.DecimalField(
        _("Amount Allocated"), decimal_places=2, max_digits=12,
        default=Decimal('0.00'))
    amount_debited = models.DecimalField(
        _("Amount Debited"), decimal_places=2, max_digits=12,
        default=Decimal('0.00'))
    amount_refunded = models.DecimalField(
        _("Amount Refunded"), decimal_places=2, max_digits=12,
        default=Decimal('0.00'))

    # Reference number for this payment source.  This is often used to look up
    # a transaction model for a particular payment partner.
    reference = models.CharField(_("Reference"), max_length=255, blank=True)

    # A customer-friendly label for the source, eg XXXX-XXXX-XXXX-1234
    label = models.CharField(_("Label"), max_length=128, blank=True)

    # A dictionary of submission data that is stored as part of the
    # checkout process, where we need to pass an instance of this class around
    submission_data = None

    # We keep a list of deferred transactions that are only actually saved when
    # the source is saved for the first time
    deferred_txns = None

    class Meta:
        app_label = 'payment'
        ordering = ['pk']
        verbose_name = _("Source")
        verbose_name_plural = _("Sources")

    def __str__(self):
        description = _("Allocation of %(amount)s from type %(type)s") % {
            'amount': currency(self.amount_allocated, self.currency),
            'type': self.source_type}
        if self.reference:
            description += _(" (reference: %s)") % self.reference
        return description

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.deferred_txns:
            for txn in self.deferred_txns:
                self._create_transaction(*txn)

    def create_deferred_transaction(self, txn_type, amount, reference=None,
                                    status=None):
        """
        Register the data for a transaction that can't be created yet due to FK
        constraints.  This happens at checkout where create an payment source
        and a transaction but can't save them until the order model exists.
        """
        if self.deferred_txns is None:
            self.deferred_txns = []
        self.deferred_txns.append((txn_type, amount, reference, status))

    def _create_transaction(self, txn_type, amount, reference='',
                            status=''):
        self.transactions.create(
            txn_type=txn_type, amount=amount,
            reference=reference, status=status)

    # =======
    # Actions
    # =======

    def allocate(self, amount, reference='', status=''):
        """
        Convenience method for ring-fencing money against this source
        """
        self.amount_allocated += amount
        self.save()
        self._create_transaction(
            Transaction.AUTHORISE, amount, reference, status)
    allocate.alters_data = True

    def debit(self, amount=None, reference='', status=''):
        """
        Convenience method for recording debits against this source
        """
        if amount is None:
            amount = self.balance
        self.amount_debited += amount
        self.save()
        self._create_transaction(
            Transaction.DEBIT, amount, reference, status)
    debit.alters_data = True

    def refund(self, amount, reference='', status=''):
        """
        Convenience method for recording refunds against this source
        """
        self.amount_refunded += amount
        self.save()
        self._create_transaction(
            Transaction.REFUND, amount, reference, status)
    refund.alters_data = True

    # ==========
    # Properties
    # ==========

    @property
    def balance(self):
        """
        Return the balance of this source
        """
        return (self.amount_allocated - self.amount_debited
                + self.amount_refunded)

    @property
    def amount_available_for_refund(self):
        """
        Return the amount available to be refunded
        """
        return self.amount_debited - self.amount_refunded


class PaymentGateWayResponse(models.Model):
    PURCHASE = 'Purchase'
    REFUND = 'Refund'
    OTHERS = 'Others'
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )
    transaction_id = models.CharField(max_length=128, null=True, verbose_name="Payment Transaction ID")
    transaction_type = models.CharField(max_length=128, choices=(
        (PURCHASE, PURCHASE),
        (REFUND, REFUND),
        (OTHERS, OTHERS),
    ), default=PURCHASE)
    source = models.ForeignKey('payment.Source', on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey('orders.Order', on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    response = models.TextField(null=True)
    payment_status = models.CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    # payee = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    parent_transaction = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} " + (
            f"with transaction id #{self.transaction_id}" if self.transaction_id else ''
        )
