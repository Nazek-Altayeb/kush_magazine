from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.CharField(max_length=1500, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
    category = models.CharField(max_length=100, default='not-categorized')
    likes = models.ManyToManyField(User, related_name='like_articles')

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    date_and_time= models.DateTimeField(default=timezone.now)
    body = models.CharField(max_length=1000, null=False, blank=False)
    article = models.ForeignKey("Article", related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    class Meta:
        ordering = ["date_and_time"]

    def __str__(self):
        return f"Comment {self.body} by {self.user}"


"""class Topic(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name"""
