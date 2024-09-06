from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # 비밀번호는 쓰기 전용
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'nickname', 'birthday', 'gender', 'PR']  # 입력 필드
        extra_kwargs = {
            'email': {'required': True},  # 이메일 필수 입력
            'first_name': {'required': True},  # 이름 필수 입력
            'nickname': {'required': True},  # 닉네임 필수 입력
            'birthday': {'required': True},  # 생일 필수 입력
            'gender': {'required': False},  # 성별 선택 입력
            'PR': {'required': False},  # 자기소개 선택 입력
        }

    # 사용자 생성 시 비밀번호 해싱 처리
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            nickname=validated_data['nickname'],
            birthday=validated_data['birthday'],
            gender=validated_data.get('gender', ''),  # 선택 입력 필드 (없으면 빈 값으로 처리)
            PR=validated_data.get('PR', '')  # 선택 입력 필드 (없으면 빈 값으로 처리)
        )
        user.set_password(validated_data['password'])  # 비밀번호 해싱
        user.save()
        return user