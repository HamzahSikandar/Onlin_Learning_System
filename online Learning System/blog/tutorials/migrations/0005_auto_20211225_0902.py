# Generated by Django 2.2.5 on 2021-12-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_auto_20211225_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='sno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
