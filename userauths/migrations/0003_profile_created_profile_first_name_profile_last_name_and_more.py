# Generated by Django 4.1.7 on 2023-04-01 00:14

from django.db import migrations, models
import userauths.models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_rename_user_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=userauths.models.user_directory_path, verbose_name='profile-pic'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_info',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
