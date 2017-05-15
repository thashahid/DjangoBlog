from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import BlogPost, UserForm, BlogForm, Comment, CommentForm

import datetime

def index(request):
    latest_posts = BlogPost.objects.order_by('-date_published')[:5]
    return render(request, 'Blog/index.html', {'posts': latest_posts})


def blog(request, year, month, post_id):
    blog = BlogPost.objects.get(pk=post_id)
    comments = Comment.objects.filter(blog=post_id).order_by('-date_posted')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            task = comment_form.save(commit=False)
            task.author = request.user
            task.blog = blog
            task.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = CommentForm()

    return render(request, 'Blog/blog.html', {'blog': blog, 'comments': comments, 'comment_form': form})


def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return HttpResponseRedirect('/')
    else:
        user_form = UserCreationForm()

    return render(request, 'Blog/signup.html', {'user_form': user_form})


@login_required(login_url='/signin')
def create(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        pub_date = datetime.datetime.now()
        if blog_form.is_valid():
            task = blog_form.save(commit=False)
            task.owner = request.user
            task.month_published = pub_date.strftime("%B")
            task.year_published = pub_date.year
            task.save()
            return HttpResponseRedirect('/')
    else:
        form = BlogForm()
    return render(request, 'Blog/create.html', {'form': form})


def year(request, year):
    blog = BlogPost.objects.filter(year_published=year)
    context = {
    'blog': blog,
    'isYear': True,
    'year': str(year)
    }
    return render(request, 'Blog/blogs.html', context)


def month(request, year, month):
    blog = BlogPost.objects.filter(year_published=year, month_published=month)
    context = {
    'blog': blog,
    'isYear': False,
    'year': str(year),
    'month': month
    }
    return render(request, 'Blog/blogs.html', context)


def user(request, un):
    user_info = User.objects.get(username=un)
    posts_owned_by_user = BlogPost.objects.filter(owner=user_info).order_by('-date_published')
    return render(request, 'Blog/user.html', {'user_info': user_info, 'posts_owned_by_user': posts_owned_by_user})
