from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Product


def product_list(request):
    product_type = request.GET.get('type', '')
    products = Product.objects.filter(is_active=True)
    if product_type:
        products = products.filter(product_type=product_type)

    return render(
        request,
        'catalog/product_list.html',
        {
            'products': products,
            'product_type': product_type,
            'page_title': 'FitForge Shop',
            'meta_description': 'Shop FitForge workout plans, nutrition plans, and fitness merchandise.',
        },
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(
        request,
        'catalog/product_detail.html',
        {
            'product': product,
            'page_title': product.name,
            'meta_description': product.description[:150],
        },
    )


def add_to_bag(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    quantity = max(1, int(request.POST.get('quantity', 1)))
    bag = request.session.get('bag', {})
    bag[str(product_id)] = bag.get(str(product_id), 0) + quantity
    request.session['bag'] = bag
    messages.success(request, f'{product.name} added to your bag.')
    return redirect('product_detail', slug=product.slug)


def view_bag(request):
    bag_items, total = get_bag_items(request)
    return render(
        request,
        'catalog/bag.html',
        {
            'bag_items': bag_items,
            'total': total,
            'page_title': 'Shopping Bag',
            'meta_description': 'Review your FitForge shopping bag before checkout.',
        },
    )


def remove_from_bag(request, product_id):
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, id=product_id)
    bag.pop(str(product_id), None)
    request.session['bag'] = bag
    messages.info(request, f'{product.name} removed from your bag.')
    return redirect('view_bag')


def get_bag_items(request):
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, id=product_id, is_active=True)
        line_total = product.price * quantity
        total += line_total
        bag_items.append({'product': product, 'quantity': quantity, 'line_total': line_total})

    return bag_items, total
