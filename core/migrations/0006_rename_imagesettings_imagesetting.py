# Generated by Django 5.0.6 on 2024-06-02 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_imagesettings_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageSettings',
            new_name='ImageSetting',
        ),
    ]
