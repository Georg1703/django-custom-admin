# Generated by Django 3.2.6 on 2021-08-30 09:56

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='images/', upload_to=store.models.user_directory_path)),
            ],
            options={
                'verbose_name_plural': 'product images',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'products'},
        ),
        migrations.AddField(
            model_name='product',
            name='default_image',
            field=models.FileField(blank=True, null=True, upload_to=store.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product'),
        ),
    ]
