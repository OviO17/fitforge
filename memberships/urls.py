from django.urls import path

from . import views

urlpatterns = [
    path('', views.membership_detail, name='membership_detail'),
    path('start/', views.start_membership, name='start_membership'),
]
