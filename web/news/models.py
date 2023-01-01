from django.urls import reverse
from django.db import models
class News(models.Model):
    choices = [('Sport','Sport'),
               ('Health','Health'),
               ('Politics','Politics'),
               ('Economics','Economics'),
               ('Technology','Technology'),]
    NewsTitle = models.CharField(max_length=100)
    NewsBody = models.TextField(default="")
    NewsClass = models.CharField(max_length = 100, choices=choices)
    ViewCounter = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200,null=True, blank = False,unique=True)
    def __str__(self):
        return self.NewsTitle
# Create your models here.
