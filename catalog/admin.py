from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'price', 'stock', 'is_featured', 'is_active')
    list_filter = ('product_type', 'is_featured', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

# Register your models here.
