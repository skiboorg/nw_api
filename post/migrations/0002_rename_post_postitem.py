# Generated by Django 3.2.4 on 2021-06-10 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='PostItem',
        ),
    ]
