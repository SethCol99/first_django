from django.urls import path
from . import views

urlpatterns = [
    path("", views.atoms),
    path('electrons', views.electrons),
    path('protons', views.protons),
    path('neutrons', views.neutrons)
]