# Generated by Django 4.2.5 on 2023-09-16 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_userprofile_address_line_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='longtitude',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='pin_code',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='state',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='province',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ward',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]