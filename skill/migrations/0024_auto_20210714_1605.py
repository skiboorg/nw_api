# Generated by Django 3.2.4 on 2021-07-14 13:05

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0023_auto_20210714_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='purpose',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Предназначение '),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='step1_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='step2_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='step3_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='step4_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='step5_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='step6_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
