# Generated by Django 3.2 on 2022-03-26 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0048_shop_reg_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopusername', models.CharField(max_length=200)),
                ('usid', models.CharField(max_length=200)),
                ('Riceqt', models.CharField(max_length=200)),
                ('Riceprc', models.CharField(max_length=200)),
                ('Whtqt', models.CharField(max_length=200)),
                ('Whtprc', models.CharField(max_length=200)),
                ('Keroqt', models.CharField(max_length=200)),
                ('Keroprc', models.CharField(max_length=200)),
                ('Ataqt', models.CharField(max_length=200)),
                ('Ataprc', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
                ('month', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('purchasecode', models.CharField(max_length=200)),
                ('status', models.CharField(default='ordered', max_length=200)),
            ],
        ),
    ]
