# Generated by Django 4.1.7 on 2023-04-03 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_like'),
        ('userauths', '0006_rename_profile_info_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favourite',
            field=models.ManyToManyField(blank=True, to='post.post'),
        ),
    ]