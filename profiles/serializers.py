from rest_framework import serializers
from .models import Profile
from accounts.models import User 


class ProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Profile
        fields = ['user', 'image', 'created_at', 'following', 'followers', 'PR',]
        read_only_fields = ['user', 'image', 'created_at', 'following', 'followers']
        # 일단은 PR만 수정 가능하도록 나머지는 읽기 전용 필드 설정 
        