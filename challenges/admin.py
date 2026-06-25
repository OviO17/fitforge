from django.contrib import admin

from .models import ChallengeCompletion, DailyChallenge


@admin.register(DailyChallenge)
class DailyChallengeAdmin(admin.ModelAdmin):
    list_display = ('active_date', 'title', 'difficulty', 'points', 'is_active')
    list_filter = ('difficulty', 'is_active', 'active_date')
    search_fields = ('title', 'description')


@admin.register(ChallengeCompletion)
class ChallengeCompletionAdmin(admin.ModelAdmin):
    list_display = ('user', 'challenge', 'completed_at')
    list_filter = ('completed_at',)
    search_fields = ('user__username', 'challenge__title')

# Register your models here.
