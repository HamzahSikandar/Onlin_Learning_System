# Generated by Django 2.2.5 on 2021-12-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0007_auto_20211226_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(default='', max_length=130),
        ),
    ]
