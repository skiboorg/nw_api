# Generated by Django 3.2.4 on 2021-06-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0016_auto_20210616_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='build',
            name='name_slug',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]
