# Generated by Django 3.2.6 on 2021-08-31 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_deposittranslation_factorytranslation_translabledepositfields_translablefactoryfields'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='factorytranslation',
            unique_together={('field', 'lang')},
        ),
    ]
