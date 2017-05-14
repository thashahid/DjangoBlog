from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogPost

def index(request):
    latest_posts = BlogPost.objects.order_by('-date_published')[:5]
    return render(request, 'Blog/index.html', {'posts': latest_posts})


def blog(request, post_id):
    blog = BlogPost.objects.get(pk=post_id)
    return render(request, 'Blog/blog.html', {'blog': blog})
