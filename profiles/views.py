from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        
        
    def put(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        