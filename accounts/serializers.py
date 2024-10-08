from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import check_password

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
    
    # 수정시 이메일과 username 중복 방지
    
    def validate_email(self, value):
        user = self.instance
        # self.instance가 None일 수 있기 때문에 이를 처리
        if user is not None and User.objects.filter(email=value).exclude(pk=user.pk).exists():
            raise serializers.ValidationError("이미 사용 중인 email 입니다.")
        elif User.objects.filter(email=value).exists():  # 새로 생성할 때 중복 검사
            raise serializers.ValidationError("이미 사용 중인 email 입니다.")
        return value
        
    def validate_username(self, value):
        user = self.instance
        # self.instance가 None일 수 있기 때문에 이를 처리
        if user is not None and User.objects.filter(username=value).exclude(pk=user.pk).exists():
            raise serializers.ValidationError("이미 사용 중인 username 입니다.")
        elif User.objects.filter(username=value).exists():  # 새로 생성할 때 중복 검사
            raise serializers.ValidationError("이미 사용 중인 username 입니다.")
        return value
    
    

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required = True, write_only =True) # 기존 비밀번호
    new_password = serializers.CharField(required = True, write_only =True) # 변경할 비밀번호
    
    def validate(self, data): # 검증 매서드
        user = self.context['request'].user
        
        if data['old_password'] == data['new_password']: # 기존 비밀번호와 변경할 비밀번호가 같으면 오류 메시지 출력
            raise serializers.ValidationError("새 패스워드는 기존 패스워드와 달라야 합니다.")

        if not check_password(data['old_password'], user.password): # 사용자가 입력한 기존 비밀번호가 해싱된 비밀번호와 일치하는지 검증
            raise serializers.ValidationError("기존 패스워드가 맞지 않습니다.")
        
        try:
            validate_password(data['new_password'], user)
        except serializers.ValidationError as e:
            raise serializers.ValidationError({'new_password': e.messages})
        
        return data
    
    def save(self):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        
        
# 회원 탈퇴시 비밀번호 검증

class UserDeleteSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True) # 비밀번호 입력을 위한 필드
    
    def validate_password(self, value):
        user = self.context['request'].user
        if not check_password(value, user.password):  # 입력된 비밀번호가 기존 비밀번호와 일치하는지 확인
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        return value