# Generated by Django 3.2.4 on 2021-07-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0012_resource_description_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='level',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
