# Generated by Django 3.2 on 2022-03-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0047_customer_reg'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_reg',
            name='Rating',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
