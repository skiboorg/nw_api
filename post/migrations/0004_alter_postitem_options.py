# Generated by Django 3.2.4 on 2021-06-24 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_postitem_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postitem',
            options={'ordering': ['order']},
        ),
    ]
