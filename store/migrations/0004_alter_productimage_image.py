# Generated by Django 3.2.6 on 2021-08-31 13:28

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='images/', upload_to=store.models.user_directory_path),
        ),
    ]
