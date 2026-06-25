from django.urls import path

from . import views

urlpatterns = [
    path('', views.workout_list, name='workout_list'),
    path('<slug:slug>/', views.workout_detail, name='workout_detail'),
    path('<slug:slug>/complete/', views.complete_workout, name='complete_workout'),
]
