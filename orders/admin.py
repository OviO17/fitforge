from django.contrib import admin

from .models import Order, OrderLineItem


class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('line_total',)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineItemInline]
    list_display = ('id', 'email', 'status', 'order_total', 'created_at')
    list_filter = ('status', 'created_at')
    readonly_fields = ('order_total', 'created_at')
    search_fields = ('email', 'full_name', 'stripe_pid')

# Register your models here.
