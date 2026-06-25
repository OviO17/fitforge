from django.contrib import messages
from django.shortcuts import redirect

from .forms import NewsletterSignupForm


def signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are signed up for FitForge updates.')
        else:
            messages.error(request, 'Please enter a valid email and consent to receive updates.')
    return redirect(request.POST.get('next', 'home'))
