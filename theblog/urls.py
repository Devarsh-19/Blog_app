import imp
from django.urls import path
from .views import AddPost, DetailView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', DetailView.as_view(), name="detail"),
    path('post/', AddPost.as_view(), name="add_post"),
]
