from django.db import models
from django.contrib.auth.models import User

# Create your models here.


"""class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.CharField(max_length=1500, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '|' + str(self.author)"""
