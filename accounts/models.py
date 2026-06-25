from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    STRENGTH = 'strength'
    FAT_LOSS = 'fat_loss'
    MOBILITY = 'mobility'
    ENDURANCE = 'endurance'

    FITNESS_GOALS = [
        (STRENGTH, 'Build strength'),
        (FAT_LOSS, 'Lose body fat'),
        (MOBILITY, 'Improve mobility'),
        (ENDURANCE, 'Improve endurance'),
    ]

    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'

    EXPERIENCE_LEVELS = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120, blank=True)
    fitness_goal = models.CharField(max_length=30, choices=FITNESS_GOALS, blank=True)
    experience_level = models.CharField(max_length=30, choices=EXPERIENCE_LEVELS, blank=True)
    dietary_preference = models.CharField(max_length=100, blank=True)
    preferred_training_style = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} profile'

# Create your models here.
