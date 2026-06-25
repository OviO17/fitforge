from django.conf import settings
from django.db import models


class ProgressPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='progress_posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    workout_focus = models.CharField(max_length=80)
    minutes_trained = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='progress/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

# Create your models here.
