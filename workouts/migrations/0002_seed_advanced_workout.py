from django.db import migrations


ADVANCED_WORKOUT = {
    'title': 'Advanced Forge Gauntlet',
    'slug': 'advanced-forge-gauntlet',
    'summary': 'A demanding strength and conditioning session for experienced members.',
    'instructions': (
        'Warm up for eight minutes.\n'
        'Complete six rounds of 12 burpees, 16 alternating lunges, 12 push-ups, '
        '20 mountain climbers, and a 60-second plank.\n'
        'Rest 90 seconds between rounds and cool down fully.'
    ),
    'duration_minutes': 50,
    'difficulty': 'advanced',
    'training_goal': 'strength and conditioning',
    'points': 60,
    'is_premium': True,
    'is_active': True,
}


def seed_advanced_workout(apps, schema_editor):
    workout_plan = apps.get_model('workouts', 'WorkoutPlan')
    workout_plan.objects.update_or_create(
        slug=ADVANCED_WORKOUT['slug'],
        defaults=ADVANCED_WORKOUT,
    )


def remove_advanced_workout(apps, schema_editor):
    workout_plan = apps.get_model('workouts', 'WorkoutPlan')
    workout_plan.objects.filter(slug=ADVANCED_WORKOUT['slug']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_advanced_workout, remove_advanced_workout),
    ]
