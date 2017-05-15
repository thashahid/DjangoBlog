from django.db import models

from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField()
    date_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
