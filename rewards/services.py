from django.db.models import Sum

from .models import RewardEvent


RANK_THRESHOLDS = [
    ('No Rank', 0),
    ('Copper', 50),
    ('Bronze', 150),
    ('Silver', 300),
    ('Gold', 500),
    ('Platinum', 800),
    ('Diamond', 1200),
]

RANK_BADGES = {
    'No Rank': 'images/ranks/no-rank.svg',
    'Copper': 'images/ranks/copper.svg',
    'Bronze': 'images/ranks/bronze.svg',
    'Silver': 'images/ranks/silver.svg',
    'Gold': 'images/ranks/gold.svg',
    'Platinum': 'images/ranks/platinum.svg',
    'Diamond': 'images/ranks/diamond.svg',
}


def get_total_points(user):
    result = RewardEvent.objects.filter(user=user).aggregate(total=Sum('points'))
    return result['total'] or 0


def get_rank_for_points(points):
    current_rank = RANK_THRESHOLDS[0][0]
    for rank_name, threshold in RANK_THRESHOLDS:
        if points >= threshold:
            current_rank = rank_name
    return current_rank


def get_next_rank(points):
    for rank_name, threshold in RANK_THRESHOLDS:
        if points < threshold:
            return rank_name, threshold, threshold - points
    return 'Diamond', 1200, 0


def get_rank_badge_path(rank_name):
    return RANK_BADGES.get(rank_name, RANK_BADGES['No Rank'])


def award_points(user, event_type, points, description, idempotency_key=''):
    if idempotency_key:
        event, _ = RewardEvent.objects.get_or_create(
            user=user,
            idempotency_key=idempotency_key,
            defaults={
                'event_type': event_type,
                'points': points,
                'description': description,
            },
        )
        return event

    return RewardEvent.objects.create(
        user=user,
        event_type=event_type,
        points=points,
        description=description,
    )
