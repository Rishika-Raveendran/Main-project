# Generated by Django 4.2.1 on 2023-05-09 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_producers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Producers',
            new_name='Producer',
        ),
    ]
