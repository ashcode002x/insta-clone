# Generated by Django 4.1.7 on 2023-04-01 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_profile_created_profile_first_name_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_info',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='url',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
