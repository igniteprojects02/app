# Generated by Django 3.1.12 on 2024-12-21 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_api', '0004_auto_20241221_1729'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='preferredsubject',
            unique_together=set(),
        ),
    ]
