from django.urls import path

from . import views

urlpatterns = [
    path('', views.challenge_list, name='challenge_list'),
    path('<int:challenge_id>/complete/', views.complete_challenge, name='complete_challenge'),
]
