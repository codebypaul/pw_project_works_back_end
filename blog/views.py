from django.shortcuts import render
from .models import Post

def all_posts(request):
    posts = Post.objects.all()

    return posts