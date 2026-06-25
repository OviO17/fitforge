from django.conf import settings
from django.db import models
from django.utils import timezone


class Membership(models.Model):
    FREE = 'free'
    ACTIVE = 'active'
    PAST_DUE = 'past_due'
    CANCELED = 'canceled'

    STATUSES = [
        (FREE, 'Free'),
        (ACTIVE, 'Active'),
        (PAST_DUE, 'Past due'),
        (CANCELED, 'Canceled'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='membership', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUSES, default=FREE)
    stripe_customer_id = models.CharField(max_length=140, blank=True)
    stripe_subscription_id = models.CharField(max_length=140, blank=True)
    current_period_end = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}: {self.get_status_display()}'

    @property
    def is_active(self):
        if self.status != self.ACTIVE:
            return False
        return not self.current_period_end or self.current_period_end >= timezone.now()

# Create your models here.
