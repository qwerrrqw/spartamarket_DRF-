from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

# 상품 목록 조회(GET) 및 상품 등록(POST)

class ProductListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # 로그인 없이 조회 가능, 등록은 로그인 필요

    def perform_create(self, serializer): # 상품 등록 시, 작성자 설정
        serializer.save(author=self.request.user)




# 상품 조회, 수정, 삭제 (GET/PUT/DELETE)

class ProductRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]  # 로그인된 사용자만 수정/삭제 가능

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        if product.author != request.user:
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        if product.author != request.user:
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)