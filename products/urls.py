from django.urls import path
from .views import ProductListCreateView, ProductRUDView, CategoryCreateView

app_name = "products"
urlpatterns = [
    path("", ProductListCreateView.as_view(), name="product_list_create_view"),
    path("<int:pk>/", ProductRUDView.as_view(), name="product_rud_view"),
    path('category/', CategoryCreateView.as_view(), name='category'),
]
