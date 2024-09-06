from django.urls import path
from . import views
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView)

appname = "accounts"
urlpatterns = [
    #
    path("", views.UserListAPIView, name="article_list"),
    path("<int:pk>/", views.UserDetailAPIView, name="article_detail"),
    
    #
    
    path("signin/", TokenObtainPairView.as_view(),  name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(),  name="token_obtain_pair"),
]
