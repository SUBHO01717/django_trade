# Generated by Django 3.2.8 on 2021-10-09 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsd_front', '0007_auto_20211009_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='DEFAULT-IMG.jpg', upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='course',
            name='resources',
            field=models.FileField(upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]