# Generated by Django 3.1.12 on 2024-12-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_api', '0003_courseproxy_preferredsubject'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferredsubject',
            name='course_code',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='preferredsubject',
            unique_together={('user', 'course_code')},
        ),
        migrations.RemoveField(
            model_name='preferredsubject',
            name='course',
        ),
    ]
