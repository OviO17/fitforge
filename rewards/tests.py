from django.contrib.auth.models import User
from django.test import TestCase

from .models import RewardEvent
from .services import award_points, get_next_rank, get_rank_for_points, get_total_points


class RewardServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='maya', password='testpass123')

    def test_points_total_and_rank_are_calculated_from_events(self):
        award_points(self.user, RewardEvent.DAILY_CHALLENGE, 15, 'Daily challenge')
        award_points(self.user, RewardEvent.WORKOUT_COMPLETED, 30, 'Workout')
        award_points(self.user, RewardEvent.PROGRESS_POST, 10, 'Progress post')

        self.assertEqual(get_total_points(self.user), 55)
        self.assertEqual(get_rank_for_points(55), 'Copper')
        self.assertEqual(get_next_rank(55), ('Bronze', 150, 95))

    def test_idempotency_key_prevents_duplicate_reward(self):
        award_points(self.user, RewardEvent.PROFILE_COMPLETED, 20, 'Profile', 'profile_completed')
        award_points(self.user, RewardEvent.PROFILE_COMPLETED, 20, 'Profile again', 'profile_completed')

        self.assertEqual(RewardEvent.objects.filter(user=self.user).count(), 1)
        self.assertEqual(get_total_points(self.user), 20)
