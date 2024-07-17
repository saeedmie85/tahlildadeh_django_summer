from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status = 'published')
    return render(request,'blog/index.html',{'posts':posts})

def post_detail(request,slug):
    # post = Post.objects.get(id = pk)
    post = get_object_or_404(Post, slug = slug, status = 'published')
    return render(request,'blog/single.html',{'post':post})