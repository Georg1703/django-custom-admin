# Generated by Django 3.2.6 on 2021-08-30 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_deposit_factory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factory',
            options={'verbose_name_plural': 'factories'},
        ),
        migrations.AddField(
            model_name='product',
            name='deposit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.deposit'),
        ),
        migrations.AddField(
            model_name='product',
            name='factory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.factory'),
        ),
    ]
