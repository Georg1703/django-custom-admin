# Generated by Django 3.2.6 on 2021-09-02 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_complete_order_placed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderstatus',
            options={'verbose_name_plural': 'order statuses'},
        ),
        migrations.CreateModel(
            name='OrderTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order')),
            ],
        ),
    ]