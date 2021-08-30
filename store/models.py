from django.db import models
from taggit.managers import TaggableManager


class Category(models.Model):
    """ table that contain possible category of product """
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class ProductLanguage(models.Model):
    name = models.CharField(max_length=2, help_text='ISO 2 Letter Language Codes')

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    if hasattr(instance, 'product'):
        return 'images/{0}/{1}'.format(instance.product.name, filename)
    else:
        return 'images/{0}/default_{1}'.format(instance, filename)


class Factory(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'factories'

    def __str__(self):
        return self.name


class Deposit(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price_per_unit = models.FloatField(null=True)
    promo_price = models.FloatField(null=True, blank=True)
    short_description = models.TextField(max_length=255, help_text='no more 255 letters', null=True)
    description = models.TextField(null=True)
    category = models.ManyToManyField(Category)
    factory = models.ForeignKey(Factory, null=True, on_delete=models.SET_NULL)
    deposit = models.ManyToManyField(Deposit, null=True)
    default_image = models.FileField(upload_to=user_directory_path, null=True)
    tags = TaggableManager()
    similars = models.ManyToManyField('self')

    def __str__(self):
        return self.name

    def categories(self):
        return ",".join([str(p) for p in self.category.all()])


class ProductProperty(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'product properties'

    def __str__(self):
        return self.name


class ProductPropertyRelation(models.Model):
    product = models.ForeignKey(Product, default=None, null=True, on_delete=models.SET_NULL)
    property = models.ForeignKey(ProductProperty, null=True, on_delete=models.SET_NULL)
    value = models.CharField(max_length=255)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, null=True, on_delete=models.SET_NULL)
    image = models.FileField(upload_to=user_directory_path, default='images/')

    def __str__(self):
        return self.product.name


class BulkSales(models.Model):
    product_count = models.IntegerField()

    def __str__(self):
        return str(self.product_count)

    class Meta:
        verbose_name_plural = 'bulk sales'


class ProductBulkSales(models.Model):
    product = models.ForeignKey(Product, default=None, null=True, on_delete=models.SET_NULL)
    product_count = models.ForeignKey(BulkSales, null=True, on_delete=models.SET_NULL)
    value = models.FloatField()

