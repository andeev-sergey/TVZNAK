from django.http import HttpResponse
from django.template import context

from main.models import *
from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.


class MainView(ListView):
    model = Subscription
    template_name = 'main.html'


def interactive(request):
    # context = {}
    return render(request, "interactive.html")


def tv_boxes(request):
    # context = {}
    return render(request, "tv-box.html")


def connect(request):
    # context = {}
    return render(request, "connect.html")


def contact(request):
    # context = {}
    return render(request, "contat.html")


def channels(request):
    # context = {}
    return render(request, "tv-box.html")


def faq(request):
    # context = {}
    return render(request, "connect.html")


def custom_page_not_found(request,exception ):
    # context = {}
    return render(request, "contat.html")

def custom_page_not_found_(request,exception ):
    # context = {}
    return render(request, "404.html")
