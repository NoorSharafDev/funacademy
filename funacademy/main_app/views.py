from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


# use TemplateView and template_name to render a file from templates directory

class Home(TemplateView):
    template_name = 'index.html'





