from django.urls import path

from .views import DogDetailView

urlpatterns: list[path] = [
    path('<int:pk>/', DogDetailView.as_view(), name='main'),
]
