from django.contrib import admin

from .models import Membership


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'current_period_end', 'updated_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'stripe_customer_id', 'stripe_subscription_id')

# Register your models here.
