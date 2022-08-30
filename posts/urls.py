from django.urls import path 
from posts.views import BoardView
urlpatterns = [path("", BoardView.as_view(), name="posts"),]