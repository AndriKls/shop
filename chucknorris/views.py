from django.shortcuts import render
import requests
from django.views.generic.base import TemplateView

# Create your views here.




class ChuckNorrisJokeView(TemplateView):
    template_name = 'chucknorris/chuck_joke.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get("https://api.chucknorris.io/jokes/random")
        if response.status_code == 200:
            data = response.json()
            context['joke'] = data.get('value')
        else:
            context['joke'] = "Oops! Couldn't fetch a Chuck Norris joke right now."
        return context
