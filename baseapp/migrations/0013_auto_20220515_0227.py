# Generated by Django 3.2.11 on 2022-05-15 01:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0012_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ManyToManyField(related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
