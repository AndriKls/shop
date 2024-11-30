from django.urls import path
from . import views

# Create your views here.


urlpatterns = [
    path('', views.SuperheroesView.as_view(), name='superheroes'),
    path('<int:pk>/', views.SuperheroDetailView.as_view(), name='superhero_detail'),
    path('create/', views.SuperheroCreateView.as_view(), name='superhero_create'),
    path('<int:pk>/update/', views.SuperheroUpdateView.as_view(), name='superhero_update'),
    path('<int:pk>/delete/', views.SuperheroDeleteView.as_view(), name='superhero_delete'),
]