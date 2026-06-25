from django.contrib import admin

from .models import ProgressPost


@admin.register(ProgressPost)
class ProgressPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'workout_focus', 'minutes_trained', 'created_at')
    list_filter = ('workout_focus', 'created_at')
    search_fields = ('title', 'content', 'user__username')

# Register your models here.
