from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = RichTextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, default='no-topic')
    likes = models.ManyToManyField(User, related_name='like_articles')

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    date_and_time= models.DateTimeField(default=timezone.now)
    body = RichTextField(null=False, blank=False)
    article = models.ForeignKey("Article", related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    class Meta:
        ordering = ["date_and_time"]

    def __str__(self):
        return f"Comment {self.body} by {self.user}"


class Topic(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
