from django.db import models


class Common(models.Model):

    name = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(Common):

    class Meta:
        db_table = 'category'

    def __str__(self):

        return self.name


class SubCategory(Common):

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        db_table = 'subcategory'

    def __str__(self):

        return self.name


class Product(Common):

    name = models.CharField(unique=True, max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=3)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)

    class Meta:
        db_table = 'product'

    def __str__(self):

        return self.name
