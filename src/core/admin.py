from django.contrib import admin
from core.models import Product, SubCategory, Category

admin.site.register([Product, SubCategory, Category])
