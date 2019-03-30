from django.shortcuts import render
from django.views.generic import ListView

from .models import Agenda

class HomePageView(ListView):
    model = Agenda
    template_name = 'app_Agenda/home.html'