# Generated by Django 3.2 on 2022-03-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0046_auto_20220324_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Cardno', models.CharField(max_length=200)),
                ('Cardtype', models.CharField(max_length=200)),
                ('No_fm', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=200, unique=True)),
                ('Address', models.CharField(max_length=200)),
                ('Username', models.CharField(max_length=200, unique=True)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
    ]
