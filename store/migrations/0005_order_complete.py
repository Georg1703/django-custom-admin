# Generated by Django 3.2.6 on 2021-09-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210902_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]