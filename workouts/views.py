from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from memberships.models import Membership
from rewards.models import RewardEvent
from rewards.services import award_points

from .models import WorkoutCompletion, WorkoutPlan


@login_required
def workout_list(request):
    workouts = WorkoutPlan.objects.filter(is_active=True)
    completed_ids = set(
        WorkoutCompletion.objects.filter(user=request.user).values_list('workout_id', flat=True)
    )
    return render(
        request,
        'workouts/workout_list.html',
        {
            'workouts': workouts,
            'completed_ids': completed_ids,
            'page_title': 'Workout Library',
            'meta_description': 'Browse FitForge workout sessions and complete them to earn reward points.',
        },
    )


@login_required
def workout_detail(request, slug):
    workout = get_object_or_404(WorkoutPlan, slug=slug, is_active=True)
    membership, _ = Membership.objects.get_or_create(user=request.user)

    if workout.is_premium and not membership.is_active:
        messages.warning(request, 'This workout requires an active FitForge membership.')
        return redirect('workout_list')

    completions = WorkoutCompletion.objects.filter(user=request.user, workout=workout)
    return render(
        request,
        'workouts/workout_detail.html',
        {
            'workout': workout,
            'completions': completions,
            'page_title': workout.title,
            'meta_description': workout.summary,
        },
    )


@login_required
def complete_workout(request, slug):
    workout = get_object_or_404(WorkoutPlan, slug=slug, is_active=True)
    membership, _ = Membership.objects.get_or_create(user=request.user)

    if request.method != 'POST':
        return redirect('workout_detail', slug=workout.slug)

    if workout.is_premium and not membership.is_active:
        messages.warning(request, 'Start a FitForge membership to complete premium workouts.')
        return redirect('workout_list')

    notes = request.POST.get('notes', '').strip()
    WorkoutCompletion.objects.create(user=request.user, workout=workout, notes=notes)
    award_points(
        request.user,
        RewardEvent.WORKOUT_COMPLETED,
        workout.points,
        f'Completed workout: {workout.title}',
    )
    messages.success(request, f'Workout complete. You earned {workout.points} points.')
    return redirect('workout_detail', slug=workout.slug)
