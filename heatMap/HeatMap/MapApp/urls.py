from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name="Home Page"),
    path('data/', views.readOutput, name='Reading Data'),
    path('data/changeData/default/', views.changeDataToDefault, name='Changing Data to Default'),
    path('data/changeData/dui/', views.changeDataToDui, name='Changing Data to Dui'),
    path('data/changeData/wildlife/', views.changeDataToWildAnimal, name='Changing Data to Wild Animal'),
    path('data/changeData/pedestrian/', views.changeDataToPedestrian, name='Changing Data to Wild Animal'),
    path('data/changeData/bicyclist/', views.changeDataToBicyclist, name='Changing Data to Wild Animal'),
    path('data/changeData/motorcycle/', views.changeDataToMotorcycle, name='Changing Data to Wild Animal'),
]