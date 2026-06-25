from datetime import date

from django.db import migrations


CHALLENGES = [
    {
        'title': 'Forge Starter Circuit',
        'description': 'Complete 12 squats, 10 push-ups, and a 30-second plank.',
        'points': 15,
        'difficulty': 'easy',
        'active_date': date(2026, 6, 27),
    },
    {
        'title': 'Core Heat Builder',
        'description': 'Complete 20 mountain climbers, 15 crunches, and a 40-second plank.',
        'points': 20,
        'difficulty': 'medium',
        'active_date': date(2026, 6, 28),
    },
    {
        'title': 'Leg Day Spark',
        'description': 'Complete 20 walking lunges, 20 calf raises, and 15 bodyweight squats.',
        'points': 20,
        'difficulty': 'medium',
        'active_date': date(2026, 6, 29),
    },
    {
        'title': 'Cardio Ember',
        'description': 'Complete 60 seconds of star jumps, 20 high knees, and 10 burpees.',
        'points': 25,
        'difficulty': 'hard',
        'active_date': date(2026, 6, 30),
    },
    {
        'title': 'Mobility Reset',
        'description': 'Spend five minutes on hip openers, hamstring stretches, and shoulder circles.',
        'points': 10,
        'difficulty': 'easy',
        'active_date': date(2026, 7, 1),
    },
    {
        'title': 'Upper Body Anvil',
        'description': 'Complete 15 push-ups, 12 chair dips, and 20 shoulder taps.',
        'points': 25,
        'difficulty': 'hard',
        'active_date': date(2026, 7, 2),
    },
]


def seed_challenges(apps, schema_editor):
    daily_challenge = apps.get_model('challenges', 'DailyChallenge')
    for challenge in CHALLENGES:
        daily_challenge.objects.update_or_create(
            active_date=challenge['active_date'],
            defaults={
                'title': challenge['title'],
                'description': challenge['description'],
                'points': challenge['points'],
                'difficulty': challenge['difficulty'],
                'is_active': True,
            },
        )


def remove_challenges(apps, schema_editor):
    daily_challenge = apps.get_model('challenges', 'DailyChallenge')
    daily_challenge.objects.filter(active_date__in=[challenge['active_date'] for challenge in CHALLENGES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_challenges, remove_challenges),
    ]
