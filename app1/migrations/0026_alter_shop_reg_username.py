# Generated by Django 3.2 on 2022-02-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_auto_20220222_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_reg',
            name='Username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
