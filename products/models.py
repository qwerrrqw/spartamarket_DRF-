from django.db import models
from django.conf import settings


class Hashtag(models.Model):
    content = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.content

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")
    hashtags = models.ManyToManyField(Hashtag, blank=True, related_name='article_hashtags')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) #카테고리가 삭제될때 게시글에서 해당 카테고리를 null 처리, 그러므로 null=True로 설정함

    def __str__(self):
        return self.title



