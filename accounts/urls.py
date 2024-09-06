from django.urls import path
from . import views
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView, TokenVerifyView,)

app_name = "accounts"
urlpatterns = [
    # list, detail, CRUD
    path("", views.UserListAPIView.as_view(), name="user_list"),
    path("<int:pk>/", views.UserDetailAPIView.as_view(), name="user_detail"),
    # 로그인
    path("signin/", TokenObtainPairView.as_view(),  name="token_obtain_pair"), #로그인 시 액세스 토큰과 리프레시 토큰을 발급
    path("token/refresh/", TokenRefreshView.as_view(),  name="token_obtain_pair"), #리프레시 토큰을 통해 새로운 액세스 토큰을 발급
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'), #특정 JWT 토큰(주로 액세스 토큰)이 유효한지 확인
    # 로그아웃
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),

]