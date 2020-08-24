from django.template.backends import django
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
# from django.shortcuts import render
from django.conf.urls import handler404



urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('interactive-tv/', interactive, name='interactive-tv'),
    path('tv-boxes/', tv_boxes, name='tv-boxes'),
    path('connect/', connect, name='connect'),
    path('contact/', contact, name='contact'),
    path('channels/', channels, name='channels'),
    path('faq/', faq, name='faq'),
    path('contact/contact_us', event_request),
    path('connect/request', buy),
    path('tv-boxes/request', buy),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
