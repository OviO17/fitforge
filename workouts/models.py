from django.conf import settings
from django.db import models


class WorkoutPlan(models.Model):
    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'

    LEVELS = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]

    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=220)
    instructions = models.TextField()
    duration_minutes = models.PositiveIntegerField(default=30)
    difficulty = models.CharField(max_length=20, choices=LEVELS)
    training_goal = models.CharField(max_length=80)
    points = models.PositiveIntegerField(default=30)
    is_premium = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['difficulty', 'title']

    def __str__(self):
        return self.title


class WorkoutCompletion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='workout_completions', on_delete=models.CASCADE)
    workout = models.ForeignKey(WorkoutPlan, related_name='completions', on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-completed_at']

    def __str__(self):
        return f'{self.user.username} completed {self.workout.title}'

# Create your models here.
