from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('api/stations/', views.stations_en_garde, name='stations_en_garde'),
]
