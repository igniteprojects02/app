# Generated by Django 3.1.12 on 2024-12-21 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
