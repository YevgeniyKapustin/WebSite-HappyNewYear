from django.urls import path

from .views import DogDetailView, redirect_to_random_dog

urlpatterns: list[path] = [
    path('', redirect_to_random_dog, name='main'),
    path('dog?id=<int:pk>/', DogDetailView.as_view(), name='dog'),
]
