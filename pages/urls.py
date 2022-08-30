# pages/urls.py

from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import HomePageView, AboutPageView
from posts.views import  BoardView
from django.contrib import admin

urlpatterns = [path("about/", AboutPageView.as_view(), name="about"),
                path("", HomePageView.as_view(), name="home"),
                path("admin/", admin.site.urls),
                path("", include("posts.urls"))
            ]