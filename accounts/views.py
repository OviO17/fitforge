from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from challenges.models import DailyChallenge
from memberships.models import Membership
from rewards.models import RewardEvent
from rewards.services import get_next_rank, get_rank_for_points, get_total_points, award_points

from .forms import RegisterForm, UserProfileForm


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your FitForge account is ready. Complete your profile to start earning points.')
            return redirect('edit_profile')
    else:
        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {
            'form': form,
            'page_title': 'Create a FitForge account',
            'meta_description': 'Create a FitForge account to track challenges, workouts, rewards, purchases, and community progress.',
        },
    )


@login_required
def dashboard(request):
    profile = request.user.userprofile
    membership, _ = Membership.objects.get_or_create(user=request.user)
    points = get_total_points(request.user)
    current_rank = get_rank_for_points(points)
    next_rank, next_threshold, points_needed = get_next_rank(points)
    progress_percent = 100 if points_needed == 0 else int((points / next_threshold) * 100)
    latest_rewards = RewardEvent.objects.filter(user=request.user)[:5]
    today_challenge = DailyChallenge.objects.filter(is_active=True).order_by('-active_date').first()

    return render(
        request,
        'accounts/dashboard.html',
        {
            'profile': profile,
            'membership': membership,
            'points': points,
            'current_rank': current_rank,
            'next_rank': next_rank,
            'points_needed': points_needed,
            'progress_percent': progress_percent,
            'latest_rewards': latest_rewards,
            'today_challenge': today_challenge,
            'page_title': 'FitForge Dashboard',
            'meta_description': 'View your FitForge rank, reward points, membership status, and daily fitness challenge.',
        },
    )


@login_required
def edit_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            if profile.full_name and profile.fitness_goal and profile.experience_level:
                award_points(
                    request.user,
                    RewardEvent.PROFILE_COMPLETED,
                    20,
                    'Completed FitForge profile',
                    idempotency_key='profile_completed',
                )
            messages.success(request, 'Profile updated.')
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)

    return render(
        request,
        'accounts/edit_profile.html',
        {
            'form': form,
            'page_title': 'Edit Profile',
            'meta_description': 'Update your FitForge fitness profile to improve workout recommendations.',
        },
    )

# Create your views here.
