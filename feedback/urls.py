from django.urls import path

from . import views

urlpatterns = [
    path('product/<int:product_id>/new/', views.create_review, name='create_review'),
    path('<int:review_id>/delete/', views.delete_review, name='delete_review'),
]
