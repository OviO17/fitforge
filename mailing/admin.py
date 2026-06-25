from django.contrib import admin

from .models import NewsletterSignup


@admin.register(NewsletterSignup)
class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'consent', 'created_at')
    list_filter = ('consent', 'created_at')
    search_fields = ('email',)

# Register your models here.
