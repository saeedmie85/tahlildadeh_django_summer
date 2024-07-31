from django.shortcuts import render
from .models import Post, Category
from django.shortcuts import get_object_or_404
# Create your views here.

def post_list(request, category_slug = None):
    posts = Post.objects.filter(status = 'published')
    if category_slug:
        category = get_object_or_404(Category,slug = category_slug)
        posts = posts.filter(category = category)
    return render(request,'blog/index.html',{'posts':posts})

def post_detail(request,year,month,day,slug):
    # post = Post.objects.get(id = pk)
    post = get_object_or_404(Post,
                                publish__year = year,
                                publish__month=month,
                                publish__day=day,
                                slug = slug, 
                                status = 'published')
    return render(request,'blog/single.html',{'post':post})