# Generated by Django 3.2.8 on 2021-10-09 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsd_front', '0004_alter_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
