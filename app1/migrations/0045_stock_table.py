# Generated by Django 3.2 on 2022-03-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0044_remove_shop_reg_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Card_type', models.CharField(max_length=200)),
                ('Riceqt', models.CharField(max_length=200)),
                ('Riceprc', models.CharField(max_length=200)),
                ('Ricestck', models.CharField(max_length=200)),
                ('Whtqt', models.CharField(max_length=200)),
                ('Whtprc', models.CharField(max_length=200)),
                ('Whtstck', models.CharField(max_length=200)),
                ('Keroqt', models.CharField(max_length=200)),
                ('Keroprc', models.CharField(max_length=200)),
                ('Kerostck', models.CharField(max_length=200)),
                ('Ataqt', models.CharField(max_length=200)),
                ('Ataprc', models.CharField(max_length=200)),
                ('Atastck', models.CharField(max_length=200)),
                ('Date', models.CharField(max_length=200)),
            ],
        ),
    ]
