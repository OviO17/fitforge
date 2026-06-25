from django.conf import settings
from django.db import models


class DailyChallenge(models.Model):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'

    DIFFICULTIES = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]

    title = models.CharField(max_length=120)
    description = models.TextField()
    points = models.PositiveIntegerField(default=15)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTIES, default=EASY)
    active_date = models.DateField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-active_date']

    def __str__(self):
        return f'{self.active_date}: {self.title}'


class ChallengeCompletion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='challenge_completions', on_delete=models.CASCADE)
    challenge = models.ForeignKey(DailyChallenge, related_name='completions', on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-completed_at']
        unique_together = ['user', 'challenge']

    def __str__(self):
        return f'{self.user.username} completed {self.challenge.title}'

# Create your models here.
