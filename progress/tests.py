from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import ProgressPost


class ProgressPostTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='owner', password='testpass123')
        self.other_user = User.objects.create_user(username='other', password='testpass123')
        self.post = ProgressPost.objects.create(
            user=self.owner,
            title='First week complete',
            content='Finished every planned session this week.',
            workout_focus='Strength',
            minutes_trained=45,
        )

    def test_owner_can_delete_progress_post(self):
        self.client.login(username='owner', password='testpass123')
        response = self.client.post(reverse('delete_progress_post', args=[self.post.id]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(ProgressPost.objects.filter(id=self.post.id).exists())

    def test_other_user_cannot_delete_progress_post(self):
        self.client.login(username='other', password='testpass123')
        response = self.client.post(reverse('delete_progress_post', args=[self.post.id]))

        self.assertEqual(response.status_code, 403)
        self.assertTrue(ProgressPost.objects.filter(id=self.post.id).exists())
