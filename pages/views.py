from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def homePageView(request):
#    return HttpResponse("Hello, World!")

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name= "home.html"

class AboutPageView(TemplateView):
    template_name: str="about.html"
