# Generated by Django 3.2.8 on 2021-10-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsd_front', '0009_auto_20211009_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='resources',
            field=models.FileField(null=True, upload_to='media/files'),
        ),
    ]