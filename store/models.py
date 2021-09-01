import uuid
from django.db import models
from django.utils.html import mark_safe
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    if hasattr(instance, 'product'):
        return 'images/{0}/{1}'.format(instance.product.name, filename)
    else:
        return 'images/{0}/default_{1}'.format(instance, filename)


def get_uuid_code(prefix: str, length: int = 10) -> str:
    return prefix + str(uuid.uuid4())[:10-len(prefix)].upper()


class SoftDeleteManager(models.Manager):
    """ The manager who rewrites the method of obtaining the objects in
    order not to display the ones with is_active = 0"""
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Category(models.Model):
    """ table that contain possible category of product """
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    objects = SoftDeleteManager()


class Factory(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'factories'

    def __str__(self):
        return self.name

    objects = SoftDeleteManager()


class Deposit(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    objects = SoftDeleteManager()


class Product(models.Model):
    name = models.CharField(max_length=255)
    price_per_unit = models.FloatField(null=True)
    promo_price = models.FloatField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    factory = models.ForeignKey(Factory, null=True, on_delete=models.SET_NULL)
    deposit = models.ManyToManyField(Deposit)
    default_image = models.FileField(upload_to=user_directory_path, null=True)
    tags = TaggableManager()
    similar_products = models.ManyToManyField('self', blank=True)
    product_code = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)

    def categories(self):
        return ",".join([str(p) for p in self.category.all()])

    def image_tag(self):
        return mark_safe(f'<a href="/media/{self.default_image}"><img src="/media/{self.default_image}" width="60" height="50"/></a>')
        image_tag.short_description = 'Image'
        image_tag.allow_tags = True

    def save(self, **kwargs):
        self.product_code = get_uuid_code(prefix='prod')
        super(Product, self).save(**kwargs)

    def __str__(self):
        return self.name

    objects = SoftDeleteManager()


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    objects = SoftDeleteManager()


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    order_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    @property
    def get_order_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_order_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    def __str__(self):
        return f'Order: {self.order_code}'

    def save(self, **kwargs):
        self.order_code = get_uuid_code(prefix='ord')
        super(Order, self).save(**kwargs)

    objects = SoftDeleteManager()


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    @property
    def get_total(self):
        total = self.product.price_per_unit * self.quantity
        return total

    def __str__(self):
        return f'OrderItem id: {self.id}'

    objects = SoftDeleteManager()


class ProductProperty(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'product properties'

    def __str__(self):
        return self.name

    objects = SoftDeleteManager()


class ProductPropertyRelation(models.Model):
    product = models.ForeignKey(Product, default=None, null=True, on_delete=models.SET_NULL)
    property = models.ForeignKey(ProductProperty, null=True, on_delete=models.SET_NULL)
    value = models.CharField(max_length=255)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to=user_directory_path, default='images/')

    def __str__(self):
        return self.product.name


class BulkSales(models.Model):
    product_count = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.product_count)

    class Meta:
        verbose_name_plural = 'bulk sales'

    objects = SoftDeleteManager()


class ProductBulkSales(models.Model):
    product = models.ForeignKey(Product, default=None, null=True, on_delete=models.SET_NULL)
    product_count = models.ForeignKey(BulkSales, null=True, on_delete=models.SET_NULL)
    value = models.FloatField()


class Language(models.Model):
    name = models.CharField(max_length=2, help_text='ISO 2 Letter Language Codes')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    objects = SoftDeleteManager()




class TranslableProductFields(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TranslableCategoryFields(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TranslableFactoryFields(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TranslableDepositFields(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TranslablePropertyFields(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductTranslation(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    field = models.ForeignKey(TranslableProductFields, null=True, on_delete=models.SET_NULL)
    lang = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    value = models.TextField()

    class Meta:
        unique_together = ['field', 'lang']

    def __str__(self):
        return self.value


class CategorytTranslation(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    field = models.ForeignKey(TranslableCategoryFields, null=True, on_delete=models.SET_NULL)
    lang = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    value = models.TextField()

    class Meta:
        unique_together = ['field', 'lang']


class FactoryTranslation(models.Model):
    factory = models.ForeignKey(Factory, null=True, on_delete=models.SET_NULL)
    field = models.ForeignKey(TranslableFactoryFields, null=True, on_delete=models.SET_NULL)
    lang = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    value = models.TextField()

    class Meta:
        unique_together = ['field', 'lang']


class DepositTranslation(models.Model):
    deposit = models.ForeignKey(Deposit, null=True, on_delete=models.SET_NULL)
    field = models.ForeignKey(TranslableDepositFields, null=True, on_delete=models.SET_NULL)
    lang = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    value = models.TextField()

    class Meta:
        unique_together = ['field', 'lang']


class PropertyTranslation(models.Model):
    property = models.ForeignKey(ProductProperty, null=True, on_delete=models.SET_NULL)
    field = models.ForeignKey(TranslablePropertyFields, null=True, on_delete=models.SET_NULL)
    lang = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    value = models.TextField()

    class Meta:
        unique_together = ['field', 'lang']