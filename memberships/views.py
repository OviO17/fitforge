from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone

from rewards.models import RewardEvent
from rewards.services import award_points

from .models import Membership


@login_required
def membership_detail(request):
    membership, _ = Membership.objects.get_or_create(user=request.user)
    return render(
        request,
        'memberships/detail.html',
        {
            'membership': membership,
            'page_title': 'FitForge Membership',
            'meta_description': 'Start a FitForge membership to unlock premium workouts and earn reward points.',
        },
    )


@login_required
def start_membership(request):
    if request.method != 'POST':
        return redirect('membership_detail')

    membership, _ = Membership.objects.get_or_create(user=request.user)
    membership.status = Membership.ACTIVE
    membership.current_period_end = timezone.now() + timedelta(days=30)
    membership.stripe_subscription_id = membership.stripe_subscription_id or 'development-subscription'
    membership.save()
    award_points(
        request.user,
        RewardEvent.SUBSCRIPTION_STARTED,
        50,
        'Started FitForge membership',
        idempotency_key='membership_started',
    )
    messages.success(request, 'Membership activated. Premium workouts are now unlocked.')
    return redirect('membership_detail')
