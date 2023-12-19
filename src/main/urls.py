from django.urls import path

from src.main.views import DogDetailView

urlpatterns: list[path] = [
    path('<id:int>/', DogDetailView.as_view(), name='main'),
]
