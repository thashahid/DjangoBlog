from django.db import models

class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField()
    date_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title
