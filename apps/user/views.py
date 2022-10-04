from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
