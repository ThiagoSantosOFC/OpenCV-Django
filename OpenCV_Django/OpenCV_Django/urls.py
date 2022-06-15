from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from videoStream import views

urlpatterns = [
     include('videoStream.urls'),
]

