# Generated by Django 5.0.6 on 2024-06-03 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('order',), 'verbose_name': 'Skill Settings'},
        ),
    ]
