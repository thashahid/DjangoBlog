from django.db import models

from django.forms import ModelForm

from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField()
    month_published = models.CharField(max_length=20, null=True)
    year_published = models.IntegerField(null=True)
    date_published = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    author = models.ForeignKey(User)
    content = models.TextField(max_length=600)
    date_posted = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(BlogPost, null=True)

    def __str__(self):
        output = "%s on %s" % (self.author, self.blog)
        return output


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['post_title', 'post_body']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        widgets = {
          'content': forms.Textarea(attrs={'rows':3, 'placeholder': 'Write a response...'}),
        }
        fields = ['content']
