# Generated by Django 4.2.1 on 2023-05-09 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_rename__id_producer_producer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='producer',
            name='username',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
