from django.shortcuts import render
import requests
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse
from django.http import HttpResponseRedirect
from.forms import WeatherSearchForm

# Create your views here.

API_KEY = "fe4e885cc104b4114c1fa726c63b1f18"



class WeatherSearchView(FormView):
    template_name = 'weather/weather.html'
    form_class = WeatherSearchForm

    def form_valid(self, form):
        city = form.cleaned_data['city']
        return HttpResponseRedirect(reverse('weather_result', kwargs={'city': city}))

    
class WeatherResultView(TemplateView):
    template_name = 'weather/result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = kwargs.get('city')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

        try:
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            context['weather'] = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'wind_direction': data['wind']['deg'],
                'icon': data['weather'][0]['icon'],
            }
        except requests.exceptions.RequestException as e:
            context['weather'] = {'error': f"Error fetching weather data: {str(e)}"}
        except KeyError:
            context['weather'] = {'error': f"Invalid response from API for city '{city}'."}

        return context
