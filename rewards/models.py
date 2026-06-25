from django.conf import settings
from django.db import models


class RewardEvent(models.Model):
    PROFILE_COMPLETED = 'profile_completed'
    DAILY_CHALLENGE = 'daily_challenge'
    WORKOUT_COMPLETED = 'workout_completed'
    PROGRESS_POST = 'progress_post'
    REVIEW_CREATED = 'review_created'
    PURCHASE_MADE = 'purchase_made'
    SUBSCRIPTION_STARTED = 'subscription_started'
    STREAK_BONUS = 'streak_bonus'

    EVENT_TYPES = [
        (PROFILE_COMPLETED, 'Profile completed'),
        (DAILY_CHALLENGE, 'Daily challenge completed'),
        (WORKOUT_COMPLETED, 'Workout completed'),
        (PROGRESS_POST, 'Progress post created'),
        (REVIEW_CREATED, 'Review created'),
        (PURCHASE_MADE, 'Purchase made'),
        (SUBSCRIPTION_STARTED, 'Subscription started'),
        (STREAK_BONUS, 'Streak bonus'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reward_events', on_delete=models.CASCADE)
    event_type = models.CharField(max_length=40, choices=EVENT_TYPES)
    points = models.PositiveIntegerField()
    description = models.CharField(max_length=180)
    idempotency_key = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'idempotency_key'],
                condition=~models.Q(idempotency_key=''),
                name='unique_reward_event_per_user_key',
            )
        ]

    def __str__(self):
        return f'{self.user.username}: {self.points} points'

# Create your models here.
