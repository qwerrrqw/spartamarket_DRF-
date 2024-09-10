from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 접근 가능

    def get(self, request, pk):
        profile = get_object_or_404(Profile, user__pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        profile = get_object_or_404(Profile, user__pk=pk)
        if request.user != profile.user:
            return Response({'detail': '수정 권한이 없습니다.'}, status=403)
        
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)