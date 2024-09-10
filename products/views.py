from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

# Create your views here.

# 페이지네이션 설정, 10개당 1장
class ProductListPagination(PageNumberPagination):
    page_size = 10



# 상품 목록 조회(GET) 및 상품 등록(POST)
class ProductListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # 로그인 없이 조회 가능, 등록은 로그인 필요


    def get_queryset(self): # 제목, 내용, 유저명 검색을 위한 쿼리셋
        queryset = Article.objects.all()
        search_query = self.request.query_params.get('q', None)
        
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |  # 제목 검색
                Q(content__icontains=search_query) |  # 내용 검색
                Q(author__username__icontains=search_query)  # 유저명 검색
            )
        return queryset

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
    
    
    # 카테고리 생성 (관리자만)
class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]  # 관리자만 카테고리 생성 가능