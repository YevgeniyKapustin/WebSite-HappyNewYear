from django.views.generic import DetailView

from .models import Dog


class DogDetailView(DetailView):
    model = Dog
    template_name = 'main/index.html'
    context_object_name = 'dog'
