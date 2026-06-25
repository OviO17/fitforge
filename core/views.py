from django.shortcuts import render

from mailing.forms import NewsletterSignupForm


def home(request):
    return render(
        request,
        'core/home.html',
        {
            'page_title': 'FitForge',
            'meta_description': 'FitForge helps members buy fitness plans, complete daily challenges, earn ranks, and join a supportive training community.',
            'newsletter_form': NewsletterSignupForm(),
        },
    )


def about(request):
    return render(
        request,
        'core/about.html',
        {
            'page_title': 'About FitForge',
            'meta_description': 'Learn about the FitForge fitness subscription model, reward ranks, daily challenges, and member community.',
        },
    )


def robots_txt(request):
    return render(request, 'core/robots.txt', content_type='text/plain')


def sitemap_xml(request):
    return render(request, 'core/sitemap.xml', content_type='application/xml')


def custom_404(request, exception):
    return render(request, '404.html', status=404)

# Create your views here.
