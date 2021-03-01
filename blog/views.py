from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
# def all_posts(request):
#     posts = Post.objects.all()

#     return posts
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/'
    }

    return Response(api_urls)