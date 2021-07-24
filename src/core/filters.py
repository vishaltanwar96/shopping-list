from django_filters import rest_framework as filters

from core.models import SubCategory


class SubCategoryFilterSet(filters.FilterSet):

    category = filters.CharFilter(field_name='category__name', lookup_expr='iexact')

    class Meta:
        model = SubCategory
        fields = ['category']


class ProductFilterSet(filters.FilterSet):

    sub_category = filters.CharFilter(field_name='sub_category__name', lookup_expr='iexact')
    category = filters.CharFilter(field_name='sub_category__category__name', lookup_expr='iexact')