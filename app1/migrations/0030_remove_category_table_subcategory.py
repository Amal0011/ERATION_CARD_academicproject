# Generated by Django 3.2 on 2022-02-22 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_category_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_table',
            name='Subcategory',
        ),
    ]
