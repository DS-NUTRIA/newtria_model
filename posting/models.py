from django.db import models
from django.contrib.auth.models import User
import os

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/posting/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'

class Reliability(models.Model):
    name = models.IntegerField(unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return f'/posting/reliability/{self.slug}'

    class Meta:
        verbose_name_plural = 'Reliabilities'

class Post(models.Model):
    title=models.CharField(max_length=30)
    reliability=models.ForeignKey(Reliability, null=True, on_delete=models.SET_NULL)
    content=models.TextField()
    head_image = models.ImageField(upload_to='posting/images/%Y/%m/%d/', blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)


    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/posting/{self.pk}/'

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
