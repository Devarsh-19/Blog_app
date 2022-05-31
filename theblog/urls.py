
from django.urls import path,include
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from .views import AddPost, DetailView, HomeView, UpdateView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', DetailView.as_view(), name="detail"),
    path('post/', AddPost.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdateView.as_view(), name="update_post"),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
