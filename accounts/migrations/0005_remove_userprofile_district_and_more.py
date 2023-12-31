# Generated by Django 4.2.5 on 2023-09-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_userprofile_city_remove_userprofile_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='district',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='province',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='ward',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='latitude',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='longtitude',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pin_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
