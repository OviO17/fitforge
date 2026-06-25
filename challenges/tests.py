from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rewards.models import RewardEvent
from rewards.services import get_total_points

from .models import ChallengeCompletion, DailyChallenge


class DailyChallengeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='sam', password='testpass123')
        self.challenge = DailyChallenge.objects.create(
            title='10 push-ups',
            description='Complete 10 controlled push-ups.',
            points=15,
            active_date=date.today(),
        )

    def test_user_can_complete_daily_challenge_once(self):
        self.client.login(username='sam', password='testpass123')
        url = reverse('complete_challenge', args=[self.challenge.id])

        self.client.post(url)
        self.client.post(url)

        self.assertEqual(ChallengeCompletion.objects.filter(user=self.user).count(), 1)
        self.assertEqual(RewardEvent.objects.filter(user=self.user).count(), 1)
        self.assertEqual(get_total_points(self.user), 15)
