from django.contrib import admin


from .models import Product, Category, ProductImage, Factory, Deposit, ProductPropertyRelation, \
    ProductProperty, BulkSales, ProductBulkSales, ProductTranslation, Language, CategorytTranslation, \
    FactoryTranslation, DepositTranslation, PropertyTranslation, Order, OrderItem, Customer, OrderStatus, \
    OrderTicket, Tag, TagTranslation


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
    exclude = ['image_tag', 'is_active', 'product_code']
    list_display = ['name', 'categories', 'default_image', 'image_tag']
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
    fields = (('name', 'link'), 'description')
    inlines = [FactoryTranslationAdmin]


class DepositTranslationAdmin(admin.StackedInline):
    extra = 1
    model = DepositTranslation


@admin.register(Deposit)
class DepositAdmin(SoftDelete):
    fields = (('name', 'link'), 'description')
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


class OrderItemAdmin(admin.StackedInline):
    extra = 1
    model = OrderItem
    exclude = ['is_active']


class OrderTicketAdmin(admin.StackedInline):
    extra = 1
    model = OrderTicket
    exclude = ['is_active', 'type', 'customer']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(type=2)


@admin.register(Order)
class OrderAdmin(SoftDelete):
    exclude = ['is_active', 'order_code', 'placed']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [OrderItemAdmin, OrderTicketAdmin]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(placed=True)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ['customer']
        return self.readonly_fields


@admin.register(Customer)
class CustomerAdmin(SoftDelete):
    exclude = ['is_active']
    # change_list_template = 'asd'


@admin.register(OrderStatus)
class OrderStatusAdmin(SoftDelete):
    fields = ['name']


class TagTranslationAdmin(admin.StackedInline):
    extra = 1
    model = TagTranslation


@admin.register(Tag)
class TagAdmin(SoftDelete):
    fields = ['name']
    inlines = [TagTranslationAdmin]