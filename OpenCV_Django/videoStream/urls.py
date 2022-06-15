from pipes import Template
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import  path
from django.views.generic import TemplateView

from videoStream import views

urlpatterns = [
   path('', include('videoStream.urls')),
]
