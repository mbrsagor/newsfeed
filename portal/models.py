from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class KeyWord(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserConfig(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_config')
    countries = models.ManyToManyField(Country)
    sources = models.ManyToManyField(Source)
    keywords = models.ManyToManyField(KeyWord)

    def __str__(self):
        return self.user.username


class NewsFeed(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=120)
    urlToImage = models.CharField(max_length=180)
    publishedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.author
