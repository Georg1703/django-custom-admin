# Generated by Django 3.2.6 on 2021-09-03 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20210903_1627'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='categoryttranslation',
            unique_together={('category', 'field', 'lang')},
        ),
        migrations.AlterUniqueTogether(
            name='deposittranslation',
            unique_together={('deposit', 'field', 'lang')},
        ),
        migrations.AlterUniqueTogether(
            name='factorytranslation',
            unique_together={('factory', 'field', 'lang')},
        ),
        migrations.AlterUniqueTogether(
            name='propertytranslation',
            unique_together={('property', 'field', 'lang')},
        ),
    ]
