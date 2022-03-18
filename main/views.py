from django.shortcuts import render
from posts import posts

from main.models import Post


def post_list(request):
    post = Post.objects.all()
    return render(request, 'blog/blog', context={'posts': posts})

