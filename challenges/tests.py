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

    def test_completed_challenge_is_replaced_by_available_challenge(self):
        replacement = DailyChallenge.objects.create(
            title='20 squats',
            description='Complete 20 steady squats.',
            points=20,
            active_date=date(2035, 1, 1),
        )
        for challenge in DailyChallenge.objects.exclude(id=replacement.id):
            ChallengeCompletion.objects.get_or_create(user=self.user, challenge=challenge)
        self.client.login(username='sam', password='testpass123')

        response = self.client.get(reverse('challenge_list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['challenges'][0], replacement)
