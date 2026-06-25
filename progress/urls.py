from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='progress_list'),
    path('new/', views.create_post, name='create_progress_post'),
    path('<int:post_id>/edit/', views.edit_post, name='edit_progress_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_progress_post'),
]
