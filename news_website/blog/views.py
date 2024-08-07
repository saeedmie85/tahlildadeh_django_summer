from django.shortcuts import render
from .models import Post, Category, Comment
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import CommentForm

# Create your views here.


def post_list(request, category_slug=None, author_pk=None):
    posts = Post.objects.filter(status="published")
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    if author_pk:
        user = get_object_or_404(User, pk=author_pk)
        posts = posts.filter(author=user)
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, year, month, day, slug, comment_id=None):
    # post = Post.objects.get(id = pk)
    post = get_object_or_404(
        Post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=slug,
        status="published",
    )
    comments = post.comments.filter(active=True)
    if request.method == "POST":
        if comment_id:
            comment = get_object_or_404(Comment, id=comment_id)
            comment_form = CommentForm(instance=comment, data=request.POST)
        else:
            comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
    else:
        comment_form = CommentForm()
        if comment_id:
            comment = get_object_or_404(Comment, id=comment_id)
            comment_form = CommentForm(instance=comment)

    return render(
        request,
        "blog/single.html",
        {"post": post, "comments": comments, "comment_form": comment_form},
    )
