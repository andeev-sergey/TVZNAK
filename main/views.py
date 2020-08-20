from django.http import HttpResponse
from django.template import context

from main.models import *
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.


class MainView(ListView):
    model = Subscription
    template_name = 'main.html'

class Two(ListView):
    model = Subscription
    template_name = 'nav.html'

