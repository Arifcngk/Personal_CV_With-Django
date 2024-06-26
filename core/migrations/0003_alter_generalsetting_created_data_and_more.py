# Generated by Django 5.0.6 on 2024-06-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_generalsettings_generalsetting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalsetting',
            name='created_data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date '),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='description',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Description '),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='name',
            field=models.CharField(blank=True, default='', help_text='This is val. of the Setting', max_length=254, verbose_name='Name '),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='parameters',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Parameter '),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='updated_data',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date '),
        ),
    ]
