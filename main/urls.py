
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
# from django.shortcuts import render
# from django.conf.urls import handler404


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('some/', Two.as_view(), name='nav')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
