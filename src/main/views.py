from random import randint

from django.shortcuts import redirect
from django.views.generic import DetailView

from .models import Dog


class DogDetailView(DetailView):
    model = Dog
    template_name = 'main/index.html'
    context_object_name = 'dog'


def redirect_to_random_dog(request):
    return redirect('dog', pk=randint(1, Dog.objects.count()))
