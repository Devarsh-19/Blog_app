from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView, DeleteView, CreateView

from theblog.forms import PostForm
from .models import Post
# # Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    contexts ={
        'b': 'post.pk',
    }
    ordering = ['-id']

class DetailView(DeleteView):
    model = Post
    template_name = 'article_details.html'
    
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add.html'
    # fields = '__all__'