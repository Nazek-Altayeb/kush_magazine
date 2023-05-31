from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.CharField(max_length=1500, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # topic = models.ForeignKey("Topic", on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
       # return reverse('article', args=str(self.pk))
        return reverse('home')


"""class Comment(models.Model):
    body = models.CharField(max_length=250, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey("Article", on_delete=models.CASCADE)"""


"""class Topic(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name"""
