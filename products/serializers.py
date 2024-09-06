from rest_framework import serializers
from .models import Hashtag, Article

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ["id", 'content']

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Article
        fields = ["id", 'title', 'content', 'created_at', 'updated_at', 'author', 'image']
        