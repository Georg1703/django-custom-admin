# Generated by Django 3.2.6 on 2021-09-10 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_count', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'bulk sales',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='store.category')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('description', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('description', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'factories',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ISO 2 Letter Language Codes', max_length=2)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=10, unique=True)),
                ('placed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'order statuses',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('promo_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('default_image', models.ImageField(null=True, upload_to=store.models.user_directory_path)),
                ('product_code', models.CharField(max_length=10, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(to='store.Category')),
                ('deposit', models.ManyToManyField(to='store.Deposit')),
                ('factory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.factory')),
                ('similar_products', models.ManyToManyField(blank=True, related_name='_store_product_similar_products_+', to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'product properties',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TranslableCategoryFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TranslableDepositFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TranslableFactoryFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TranslableProductFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TranslablePropertyFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TagTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.translablepropertyfields')),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.language')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPropertyRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.language')),
                ('product', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.productproperty')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/', upload_to=store.models.user_directory_path)),
                ('product', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBulkSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('product', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
                ('product_count', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.bulksales')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='store.Tag'),
        ),
        migrations.CreateModel(
            name='OrderTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Order Status'), (2, 'Message')], default=2)),
                ('message', models.TextField(null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.orderstatus'),
        ),
        migrations.CreateModel(
            name='PropertyTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.translablepropertyfields')),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.language')),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.productproperty')),
            ],
            options={
                'unique_together': {('property', 'field', 'lang')},
            },
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.translableproductfields')),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.language')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
            options={
                'unique_together': {('product', 'field', 'lang')},
            },
        ),
        migrations.CreateModel(
            name='FactoryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('factory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.factory')),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.translablefactoryfields')),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.language')),
            ],
            options={
                'unique_together': {('factory', 'field', 'lang')},
            },
        ),
        migrations.CreateModel(
            name='DepositTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('deposit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.deposit')),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.translabledepositfields')),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.language')),
            ],
            options={
                'unique_together': {('deposit', 'field', 'lang')},
            },
        ),
        migrations.CreateModel(
            name='CategorytTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.category')),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.translablecategoryfields')),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.language')),
            ],
            options={
                'unique_together': {('category', 'field', 'lang')},
            },
        ),
    ]
