from rest_framework import serializers
from .models import Profile
from accounts.models import User 


class ProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Profile
        fields = ['user', 'image', 'created_at', 'following', 'followers']