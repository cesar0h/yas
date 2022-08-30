import imp
from re import template
from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView

class BoardView(ListView):
    model=Post
    template_name="posts.html"
    