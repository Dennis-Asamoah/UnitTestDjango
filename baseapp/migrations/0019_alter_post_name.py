# Generated by Django 3.2.11 on 2022-05-21 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0018_auto_20220521_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]