from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'fitness_goal', 'experience_level', 'updated_at')
    list_filter = ('fitness_goal', 'experience_level')
    search_fields = ('user__username', 'full_name', 'dietary_preference')

# Register your models here.
