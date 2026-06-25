from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Product
from rewards.models import RewardEvent
from rewards.services import award_points

from .forms import ReviewForm
from .models import Review


@login_required
def create_review(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    review = Review.objects.filter(product=product, user=request.user).first()
    is_new_review = review is None

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            saved_review = form.save(commit=False)
            saved_review.product = product
            saved_review.user = request.user
            saved_review.save()
            if is_new_review:
                award_points(
                    request.user,
                    RewardEvent.REVIEW_CREATED,
                    10,
                    f'Reviewed product: {product.name}',
                    idempotency_key=f'review_{saved_review.id}',
                )
                messages.success(request, 'Review published. You earned 10 points.')
            else:
                messages.success(request, 'Review updated.')
            return redirect('product_detail', slug=product.slug)
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        'feedback/review_form.html',
        {
            'form': form,
            'product': product,
            'page_title': 'Product Review',
            'meta_description': f'Review {product.name} on FitForge.',
        },
    )


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user and not request.user.is_staff:
        return HttpResponseForbidden('You can only delete your own reviews.')

    product = review.product
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted.')
        return redirect('product_detail', slug=product.slug)

    return render(request, 'feedback/confirm_delete.html', {'review': review})
