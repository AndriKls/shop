from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChuckNorrisJokeView.as_view(), name="chuck"), 
]
