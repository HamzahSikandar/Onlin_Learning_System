# Generated by Django 2.2.5 on 2021-12-28 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0008_course_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='title',
            new_name='Course',
        ),
    ]