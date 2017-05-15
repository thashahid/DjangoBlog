from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import BlogPost, UserForm

def index(request):
    latest_posts = BlogPost.objects.order_by('-date_published')[:5]
    return render(request, 'Blog/index.html', {'posts': latest_posts})


def blog(request, post_id):
    blog = BlogPost.objects.get(pk=post_id)
    return render(request, 'Blog/blog.html', {'blog': blog})


def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return HttpResponseRedirect('/')
    else:
        user_form = UserCreationForm()

    return render(request, 'Blog/signup.html', {'user_form': user_form})
