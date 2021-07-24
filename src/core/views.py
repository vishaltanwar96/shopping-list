from rest_framework.generics import ListAPIView, ListCreateAPIView

from core.models import Category, SubCategory, Product
from core.filters import SubCategoryFilterSet, ProductFilterSet
from core.serializers import CategorySerializer, SubCategorySerializer, ProductSerializer


class CategoryListAPIView(ListAPIView):
    """List all the categories"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListAPIView(ListAPIView):
    """Lists all the subcategories, can also filter subcategories for a provided category"""

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filterset_class = SubCategoryFilterSet


class ProductListAPIView(ListCreateAPIView):
    """
    /GET List all the Products, filter all the products under a category or under a sub category\n
    /POST Create a new product under a specified subcategory
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilterSet
