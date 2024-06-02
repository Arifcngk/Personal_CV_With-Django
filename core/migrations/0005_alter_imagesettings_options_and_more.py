# Generated by Django 5.0.6 on 2024-06-02 09:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_imagesettings_alter_generalsetting_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesettings',
            options={'ordering': ('name',), 'verbose_name': 'Image Settings'},
        ),
        migrations.AddField(
            model_name='imagesettings',
            name='created_data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Date '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagesettings',
            name='updated_data',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date '),
        ),
    ]
