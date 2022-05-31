from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from  .forms import PostForm, EditForm
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
    ordering = ['-post_date']

class DetailView(DeleteView):
    model = Post
    template_name = 'article_details.html'
    
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add.html'
    # fields = '__all__'
    
class UpdateView(UpdateView):
    template_name = 'update_post.html'
    model = Post
    form_class= EditForm
    
