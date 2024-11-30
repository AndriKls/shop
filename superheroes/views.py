from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Superhero


class SuperheroesView(ListView):
    model = Superhero
    template_name = 'superheroes/superheroes.html'
    context_object_name = 'superheroes'


class SuperheroDetailView(DetailView):
    model = Superhero
    template_name = 'superheroes/superhero_detail.html'
    context_object_name = 'hero'

class SuperheroCreateView(CreateView):
    model = Superhero
    fields = '__all__'
    template_name = 'superheroes/superhero_form.html'
    success_url = reverse_lazy('superheroes')
    context_object_name = 'hero'


class SuperheroUpdateView(UpdateView):
    model = Superhero
    fields = '__all__'
    template_name = 'superheroes/superhero_form.html'
    success_url = reverse_lazy('superheroes')
    context_object_name = 'hero'


class SuperheroDeleteView(DeleteView):
    model = Superhero
    template_name = 'superheroes/superhero_delete.html'
    success_url = reverse_lazy('superheroes')
    context_object_name = 'hero'

