# Generated by Django 3.2.6 on 2021-09-15 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_historicalorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderticket',
            name='type',
        ),
    ]