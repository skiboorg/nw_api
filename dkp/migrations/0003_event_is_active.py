# Generated by Django 3.2.4 on 2021-06-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dkp', '0002_auto_20210624_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]