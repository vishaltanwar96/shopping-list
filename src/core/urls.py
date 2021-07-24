from django.urls import path

from core.views import CategoryListAPIView, SubCategoryListAPIView, ProductListAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='list-categories'),
    path('subcategories/', SubCategoryListAPIView.as_view(), name='list-subcategories'),
    path('products/', ProductListAPIView.as_view(), name='list-create-product'),
]
