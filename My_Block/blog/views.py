from django.db import models
from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()

    context = {
        "post": posts
    }

    return render(request, "blog/index.htm", context)
