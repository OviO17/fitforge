from decimal import Decimal

from django.conf import settings
from django.db import models

from catalog.models import Product


class Order(models.Model):
    PENDING = 'pending'
    PAID = 'paid'
    FAILED = 'failed'

    STATUSES = [
        (PENDING, 'Pending'),
        (PAID, 'Paid'),
        (FAILED, 'Failed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    street_address = models.CharField(max_length=180)
    town_or_city = models.CharField(max_length=80)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=80, default='United Kingdom')
    stripe_pid = models.CharField(max_length=180, blank=True)
    status = models.CharField(max_length=20, choices=STATUSES, default=PENDING)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Order #{self.id}'

    def update_total(self):
        total = sum(item.line_total for item in self.line_items.all())
        self.order_total = Decimal(total)
        self.save(update_fields=['order_total'])


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, related_name='line_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.line_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
        self.order.update_total()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

# Create your models here.
