# Generated by Django 3.2.6 on 2021-09-03 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210903_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderticket',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
