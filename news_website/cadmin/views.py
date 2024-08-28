from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView

# Create your views here.


class PostList(ListView):
    model = Post
    template_name = "cadmin/index.html"
    context_object_name = "posts"
