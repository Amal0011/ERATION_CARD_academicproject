# Generated by Django 3.2 on 2022-02-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0039_auto_notification_table_autoid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto_notification_table',
            name='orid',
            field=models.CharField(default='', max_length=200),
        ),
    ]
