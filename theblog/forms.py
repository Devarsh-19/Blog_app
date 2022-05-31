import imp
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'author': forms.Select(attrs={'class': 'form-control-sm'}),
            'body': forms.Textarea(attrs={'class': 'form-control-sm'}),
        }