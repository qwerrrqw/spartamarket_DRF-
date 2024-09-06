from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.



        
class UserListAPIView(APIView):
    
    def get(self, request): # 회원 리스트
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request): # 회원 생성
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class UserDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)
    
    def get(self, request, pk): # 유저 상세 페이지
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk): # 회원 정보 수정
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        
    def delete(self, request, pk): # 회원 탈퇴
        user = self.get_object(pk)
        user.delete()
        data = {"delete": f"user({pk}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)