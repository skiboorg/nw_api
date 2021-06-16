# Generated by Django 3.2.4 on 2021-06-14 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guild', '0005_guild_style'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guild',
            options={'ordering': ['-rating']},
        ),
        migrations.AddField(
            model_name='guildfeedback',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
