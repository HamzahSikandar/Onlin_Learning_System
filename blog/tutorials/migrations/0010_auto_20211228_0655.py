# Generated by Django 2.2.5 on 2021-12-28 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0009_auto_20211228_0654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Course',
            new_name='title',
        ),
    ]
