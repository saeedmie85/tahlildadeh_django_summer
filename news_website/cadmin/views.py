from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = "cadmin/index.html"
    context_object_name = "posts"
