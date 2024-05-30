# Generated by Django 3.2 on 2022-02-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0031_auto_20220222_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shop_usernm', models.CharField(max_length=200)),
                ('Product_name', models.CharField(max_length=200)),
                ('Category', models.CharField(max_length=200)),
                ('Sub_Category', models.CharField(max_length=200)),
                ('Price', models.CharField(max_length=200)),
                ('Info', models.CharField(max_length=200)),
                ('Stock', models.CharField(max_length=200)),
                ('Img_path', models.CharField(max_length=200)),
            ],
        ),
    ]