from django.db import models


class NewsletterSignup(models.Model):
    email = models.EmailField(unique=True)
    consent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email

# Create your models here.
