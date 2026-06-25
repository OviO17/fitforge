from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from rewards.models import RewardEvent
from rewards.services import award_points

from .forms import ProgressPostForm
from .models import ProgressPost


@login_required
def post_list(request):
    posts = ProgressPost.objects.select_related('user')
    return render(
        request,
        'progress/post_list.html',
        {
            'posts': posts,
            'page_title': 'Community Progress',
            'meta_description': 'Share and browse FitForge member progress updates.',
        },
    )


@login_required
def create_post(request):
    if request.method == 'POST':
        form = ProgressPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            award_points(
                request.user,
                RewardEvent.PROGRESS_POST,
                10,
                f'Shared progress post: {post.title}',
                idempotency_key=f'progress_post_{post.id}',
            )
            messages.success(request, 'Progress update shared. You earned 10 points.')
            return redirect('progress_list')
    else:
        form = ProgressPostForm()

    return render(request, 'progress/post_form.html', {'form': form, 'form_title': 'Share progress'})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(ProgressPost, id=post_id)
    if post.user != request.user and not request.user.is_staff:
        return HttpResponseForbidden('You can only edit your own progress posts.')

    if request.method == 'POST':
        form = ProgressPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Progress update saved.')
            return redirect('progress_list')
    else:
        form = ProgressPostForm(instance=post)

    return render(request, 'progress/post_form.html', {'form': form, 'form_title': 'Edit progress'})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(ProgressPost, id=post_id)
    if post.user != request.user and not request.user.is_staff:
        return HttpResponseForbidden('You can only delete your own progress posts.')

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Progress update deleted.')
        return redirect('progress_list')

    return render(request, 'progress/confirm_delete.html', {'post': post})
