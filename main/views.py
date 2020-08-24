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
    context = {'box': TvBox.objects.all()}
    return render(request, "tv-box.html", context)


def connect(request):
    context = {'subs': Subscription.objects.all()}
    return render(request, "connect.html", context)


def contact(request):
    context = {'contacts': Contact.objects.all()[:1]}
    return render(request, "contat.html", context)


def channels(request):
    context = {'channels': Channel.objects.all()}
    return render(request, "channels.html", context)


def faq(request):
    # context = {}
    return render(request, "faq.html")


def custom_page_not_found(request, exception):
    context = {'contacts': Contact.objects.all()[1]}
    return render(request, "contat.html", context)


def custom_page_not_found_(request, exception):
    # context = {}
    return render(request, "404.html")


def event_request(request):
    if request.POST:
        massage = request.POST.get('massege')
        ContactUs.objects.create(
            massege=massage,
        )
        return HttpResponse("ok", content_type="text/html")
    else:
        return HttpResponse("no", content_type="text/html")

def buy(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        Request.objects.create(
            name=name,
            email=email,
            massage=massage,
        )
        return HttpResponse("ok", content_type="text/html")
    else:
        return HttpResponse("no", content_type="text/html")

