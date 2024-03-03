from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]

urlpatterns = [
    path('api/products/', views.ProductListAPIView.as_view(), name='product-list'),
]

