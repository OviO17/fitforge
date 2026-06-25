from django.contrib import admin

from .models import RewardEvent


@admin.register(RewardEvent)
class RewardEventAdmin(admin.ModelAdmin):
    list_display = ('user', 'event_type', 'points', 'description', 'created_at')
    list_filter = ('event_type', 'created_at')
    search_fields = ('user__username', 'description')

# Register your models here.
