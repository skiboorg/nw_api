# Generated by Django 3.2.4 on 2021-07-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0026_build_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='build',
            options={'ordering': ['-rating']},
        ),
        migrations.AddField(
            model_name='buildfeedback',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='build',
            name='total_rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг Всего'),
        ),
        migrations.AlterField(
            model_name='build',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='Голосов'),
        ),
    ]