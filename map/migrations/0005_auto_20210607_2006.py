# Generated by Django 3.2.4 on 2021-06-07 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20210607_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcecategory',
            name='type',
        ),
        migrations.AddField(
            model_name='resourcetype',
            name='category',
            field=models.ManyToManyField(blank=True, to='map.ResourceCategory'),
        ),
    ]
