# Generated by Django 3.2.11 on 2022-05-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0014_remove_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.CharField(choices=[('published', 'Pusblished'), ('dennis', 'Dennis')], max_length=200, null=True),
        ),
    ]
