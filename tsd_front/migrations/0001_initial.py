# Generated by Django 3.2.8 on 2021-10-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(upload_to='files/courses_thumbnails')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('resources', models.FileField(upload_to='files/course_resources')),
                ('course_duration', models.CharField(max_length=100)),
            ],
        ),
    ]
