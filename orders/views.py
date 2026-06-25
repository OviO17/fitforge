from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
import stripe

from catalog.views import get_bag_items
from rewards.models import RewardEvent
from rewards.services import award_points

from .forms import OrderForm
from .models import Order, OrderLineItem


@login_required
def checkout(request):
    bag_items, total = get_bag_items(request)
    if not bag_items:
        messages.info(request, 'Your bag is empty.')
        return redirect('product_list')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            if settings.STRIPE_SECRET_KEY:
                stripe.api_key = settings.STRIPE_SECRET_KEY
                intent = stripe.PaymentIntent.create(
                    amount=int(total * 100),
                    currency='gbp',
                    metadata={'username': request.user.username},
                )
                order.stripe_pid = intent.id
            else:
                order.stripe_pid = 'development-payment'
            order.status = Order.PAID
            order.save()

            for item in bag_items:
                OrderLineItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                )

            award_points(
                request.user,
                RewardEvent.PURCHASE_MADE,
                25,
                f'Completed purchase #{order.id}',
                idempotency_key=f'purchase_{order.id}',
            )
            request.session['bag'] = {}
            messages.success(request, 'Payment successful. Your order has been saved.')
            return redirect('checkout_success', order_id=order.id)
    else:
        profile = request.user.userprofile
        form = OrderForm(initial={'email': request.user.email, 'full_name': profile.full_name})

    return render(
        request,
        'orders/checkout.html',
        {
            'form': form,
            'bag_items': bag_items,
            'total': total,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'page_title': 'Checkout',
            'meta_description': 'Complete your FitForge order securely.',
        },
    )


@login_required
def checkout_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(
        request,
        'orders/success.html',
        {
            'order': order,
            'page_title': 'Order Complete',
            'meta_description': 'Your FitForge order has been completed successfully.',
        },
    )
