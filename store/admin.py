from django.contrib import admin


from .models import Product, Category, ProductImage, Factory, Deposit, ProductPropertyRelation, \
    ProductProperty, BulkSales, ProductBulkSales, ProductTranslation, Language, CategorytTranslation, \
    FactoryTranslation, DepositTranslation, PropertyTranslation


class SoftDelete(admin.ModelAdmin):
    """ The class who rewrites the method of obtaining the objects in
    order not to display the ones with is_active = 0 """
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_active=True)

    def delete_queryset(self, request, queryset):
        queryset.update(is_active=False)

    class Meta:
        abstract = True


class ProductImageAdmin(admin.StackedInline):
    extra = 1
    model = ProductImage


class ProductPropertyRelationAdmin(admin.StackedInline):
    extra = 1
    model = ProductPropertyRelation


class ProductBulkSalesAdmin(admin.StackedInline):
    extra = 1
    model = ProductBulkSales


class ProductTranslationAdmin(admin.StackedInline):
    extra = 1
    model = ProductTranslation


@admin.register(Product)
class ProductAdmin(SoftDelete):
    fields = ['name', 'price_per_unit', 'promo_price', 'category',
              'factory', 'deposit', 'default_image', 'tags', 'similar_products',
              'product_code', 'image_tag']
    list_display = ['name', 'categories', 'default_image', 'image_tag']
    readonly_fields = ('product_code', 'image_tag')
    inlines = [ProductImageAdmin, ProductPropertyRelationAdmin, ProductBulkSalesAdmin, ProductTranslationAdmin]

    class Meta:
        model = Product


class CategoryTranslationAdmin(admin.StackedInline):
    extra = 1
    model = CategorytTranslation


@admin.register(Category)
class CategoryAdmin(SoftDelete):
    fields = ['name', 'parent']
    inlines = [CategoryTranslationAdmin]


class FactoryTranslationAdmin(admin.StackedInline):
    extra = 1
    model = FactoryTranslation


@admin.register(Factory)
class FactoryAdmin(SoftDelete):
    fields = ['name', 'link', 'description']
    inlines = [FactoryTranslationAdmin]


class DepositTranslationAdmin(admin.StackedInline):
    extra = 1
    model = DepositTranslation


@admin.register(Deposit)
class DepositAdmin(SoftDelete):
    fields = ['name', 'link', 'description']
    inlines = [DepositTranslationAdmin]


class PropertyTranslationAdmin(admin.StackedInline):
    extra = 1
    model = PropertyTranslation


@admin.register(ProductProperty)
class ProductPropertyAdmin(SoftDelete):
    fields = ['name']
    inlines = [PropertyTranslationAdmin]


@admin.register(BulkSales)
class BulkSalesAdmin(SoftDelete):
    fields = ['product_count']


@admin.register(Language)
class LanguageAdmin(SoftDelete):
    fields = ['name']