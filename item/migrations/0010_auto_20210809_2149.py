# Generated by Django 3.2.4 on 2021-08-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_auto_20210809_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='rarity',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='tier',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='perk',
            name='fishRarityRollModifier',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='perk',
            name='fishSizeRollModifier',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='perk',
            name='rarity',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='perk',
            name='tier',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
    ]
