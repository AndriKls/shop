from django.urls import path
from . import views

urlpatterns = [
    path('', views.WeatherSearchView.as_view(), name='weather_search'),
    path('result/<str:city>/', views.WeatherResultView.as_view(), name='weather_result'),

]
