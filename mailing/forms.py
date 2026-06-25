from django import forms

from .models import NewsletterSignup


class NewsletterSignupForm(forms.ModelForm):
    consent = forms.BooleanField(
        required=True,
        label='I agree to receive FitForge fitness and nutrition emails.',
    )

    class Meta:
        model = NewsletterSignup
        fields = ['email', 'consent']
