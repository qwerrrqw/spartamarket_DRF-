from rest_framework import serializers
from .models import Hashtag, Article, Category

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ["id", 'content']



class CategorySerializer(serializers.ModelSerializer):  # 카테고리 시리얼라이저
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at'] 
        
        
class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)  # 카테고리를 선택할 수 있도록 category_id를 PrimaryKeyRelatedField로 설정하고 카테고리의 쿼리셋을 받아옴
    
    class Meta:
        model = Article
        fields = ["id", 'title', 'content', 'created_at', 'updated_at', 'author', 'image', 'category', 'category_id']
        
        
