from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from rewards.models import RewardEvent
from rewards.services import award_points

from .models import ChallengeCompletion, DailyChallenge


@login_required
def challenge_list(request):
    completed_ids = set(
        ChallengeCompletion.objects.filter(user=request.user).values_list('challenge_id', flat=True)
    )
    available_challenges = list(
        DailyChallenge.objects.filter(is_active=True)
        .exclude(id__in=completed_ids)
        .order_by('?')[:6]
    )
    completed_challenges = list(
        DailyChallenge.objects.filter(is_active=True, id__in=completed_ids)
        .order_by('-active_date')[:4]
    )
    challenges = available_challenges + completed_challenges
    return render(
        request,
        'challenges/challenge_list.html',
        {
            'challenges': challenges,
            'completed_ids': completed_ids,
            'page_title': 'Daily Challenges',
            'meta_description': 'Complete FitForge daily challenges to earn reward points and build consistency.',
        },
    )


@login_required
def complete_challenge(request, challenge_id):
    challenge = get_object_or_404(DailyChallenge, id=challenge_id, is_active=True)
    if request.method != 'POST':
        return redirect('challenge_list')

    completion, created = ChallengeCompletion.objects.get_or_create(
        user=request.user,
        challenge=challenge,
    )

    if created:
        award_points(
            request.user,
            RewardEvent.DAILY_CHALLENGE,
            challenge.points,
            f'Completed daily challenge: {challenge.title}',
            idempotency_key=f'daily_challenge_{challenge.id}',
        )
        messages.success(request, f'Challenge complete. You earned {challenge.points} points.')
    else:
        messages.info(request, 'You have already completed this challenge.')

    return redirect('challenge_list')

# Create your views here.
