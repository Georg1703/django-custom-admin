from django.contrib import admin
from .models import Product, Category, ProductImage, ProductLanguage, Factory, Deposit, ProductPropertyRelation, \
    ProductProperty, BulkSales, ProductBulkSales


class ProductImageAdmin(admin.StackedInline):
    extra = 1
    model = ProductImage


class ProductPropertyRelationAdmin(admin.StackedInline):
    extra = 1
    model = ProductPropertyRelation


class ProductBulkSalesAdmin(admin.StackedInline):
    extra = 1
    model = ProductBulkSales


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'categories', 'description', 'default_image']
    inlines = [ProductImageAdmin, ProductPropertyRelationAdmin, ProductBulkSalesAdmin]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductProperty)
admin.site.register(BulkSales)
# admin.site.register(ProductLanguage)
admin.site.register(Factory)
admin.site.register(Deposit)