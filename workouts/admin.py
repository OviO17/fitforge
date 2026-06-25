from django.contrib import admin

from .models import WorkoutCompletion, WorkoutPlan


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'training_goal', 'points', 'is_premium', 'is_active')
    list_filter = ('difficulty', 'is_premium', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'summary', 'training_goal')


@admin.register(WorkoutCompletion)
class WorkoutCompletionAdmin(admin.ModelAdmin):
    list_display = ('user', 'workout', 'completed_at')
    list_filter = ('completed_at',)
    search_fields = ('user__username', 'workout__title', 'notes')

# Register your models here.
